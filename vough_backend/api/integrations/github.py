from typing import Union
import os
import requests
from requests import Response
import requests_cache
from urllib.parse import urljoin
from vough_backend.settings import GITHUB_TOKEN, GITHUB_API_URL, CACHE_TTL



# cache settings
requests_cache.install_cache('github_cache', backend='sqlite3', expire_after=CACHE_TTL)


class GithubApi:
    API_URL = os.getenv(GITHUB_API_URL)
    GITHUB_TOKEN = os.getenv(GITHUB_TOKEN)

    def get_organization(self, login: str) -> Union[Response, None]:
        """Busca uma organização no Github

        :login: login da organização no Github
        """
        hearders = {
            "Authorization": "token" + GITHUB_TOKEN,
            "Accept": "Application/vnd.github.v3+json"
        }

        url = urljoin(GITHUB_API_URL, f'/orgs/{login}')
        response = requests.get(url=url, headers=hearders)

        if response.ok:
            return response
        
        return None

      

    def get_organization_public_members(self, login: str) -> int:
        """Retorna todos os membros públicos de uma organização

        :login: login da organização no Github
        """
        
        url = urljoin(GITHUB_API_URL, f'/orgs/{login}/public_members')
        response = requests.get(url=url, headers={'Authorization': f'token {GITHUB_TOKEN}'})

        if response.ok:
            return response

        return None
    
    
        
    def get_name(self, org: dict) -> str:
        """
        Retorna o nome da organização
        :org: Dicionário Json da organização obtido da função get_organization()
        """
        
        name = org.get('name') or ""

        return name
    


    def get_score(self, org: dict, members: dict) -> int:
        """
        Retorna o cálculo da prioridade (score) através da soma de repositórios e a quantidade de membros públicos
        :org: Dicionário Json da organização obtido da função get_organization()
        :members: Dicionário Json dos membros da organização obtido da função get_organization_public_members()
        """
        public_repos = org.get('public_repos') or 0
        public_members = len(members)

        return public_members + public_repos
