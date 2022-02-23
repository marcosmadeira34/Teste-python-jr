from rest_framework import viewsets, status, views
from rest_framework.views import Response
from drf_spectacular.utils import extend_schema
from django.utils.decorators import method_decorator
from django.views.decorators import cache
from .integrations.github import GithubApi
from vough_backend.settings import CACHE_TTL
from . import models, serializers


# TODOS:
# 1 - Buscar organização pelo login através da API do Github
# 2 - Armazenar os dados atualizados da organização no banco
# 3 - Retornar corretamente os dados da organização
# 4 - Retornar os dados de organizações ordenados pelo score na listagem da API

@extend_schema(tags=['orgs', ])
class OrganizationViewSet(viewsets.ModelViewSet):

    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer
    lookup_field = "login"
    permission_classes = []
    authentication_classes = []

    @extend_schema(
        summary='Consulta clientes ordenados pela prioridade',
        description='Consulta clientes ordenados pela prioridade (score), da maior para a menor.',
    )

    
    # retorna lista de organizações ordenadas pelo score
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().order_by('-score'))

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializers = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializers.data)

        serializers = self.get_serializer(queryset, many=True)
        return views.Response(serializers.data)    
    
    
    @extend_schema(
        summary=('Consulta um cliente específico'),
        description='Consulta um cliente específico através do nome (login)'
    )


    #Consulta api via login retornando uma organização. Caso esteja no banco de dados, seus dados de
    #serão atualizados, caso contrário, seja criada com seus dados de retorno da API do Github.
    
       
    @method_decorator(cache.cache_page(CACHE_TTL))
    def retrieve(self, request, *args, **kwargs):
        api = GithubApi()
        login = self.kwargs.get(self.lookup_field).lower()
        organization = api.get_organization(login)
        public_members = api.get_organization_public_members(login)

        
        # caso login inválido, retorna HTTP 404
        if not organization or not public_members:
            return views.Response({'login': login, 'message': 'Nenhuma organização localizada com o login informado'}, status=404)

        name = api.get_name(organization.json())        
        score = api.get_score(organization.json())
        status_retrieve = status.HTTP_200_OK

        
        # atualização de dados da organização no banco de dados, caso exista.
        try:
            models.Organization.objects.filter(login=login).update(login=login, name=name, score=score)
            instance = generics.get_object_or_404(models.Organization, login=login)
        except:
        # armazenar nova org via dados API
            instance = models.Organization.objects.create(login=login, name=name, score=score)
            status_retrieve = status.HTTP_201_CREATED

        serializer = self.get_serializer(instance)
        return views.Response(serializer.data, status_retrieve)


    @extend_schema(
        summary = ('Deleta um cliente em específico'),
        description = 'Deleta cliente à partir da busca login'
    )

    def destroy(self, request, *args, **kwargs):
        login = self.kwargs.get(self.lookup_field).lower()  
        try:
            instance = generic.get_object_or_404(models.Organization, login=login)
        except:
            return views.Response({'login': login, 'message': 'Organização inexistente ou não consultada anteriormente'}, status=404)

        self.perform_destroy(instance)
        return views.Response(status=status.HTTP_204_NO_CONTENT)


    
    # percorre todos os dados da função get_queryset e atualiza cache após alguma alteração no banco
    def get_queryset(self):
        queryset = models.Organization.objects.all()
        return queryset

