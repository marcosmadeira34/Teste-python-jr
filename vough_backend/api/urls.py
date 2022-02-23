from django.urls import path, include
from . import views
from api.routes import CustomRouter
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView




routers = CustomRouter()
routers.register('orgs', views.OrganizationViewSet)


# rota de documentação swagger-ui (user interface) 
urlpatterns =[
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(), name='swagger-ui'),
    path('', include(routers.urls))
]




