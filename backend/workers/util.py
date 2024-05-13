import os
import json
import requests
from models.repositoryInfo import RepositoryInfo
from workers.githubResponse import GithubResponse


class Util:

    '''
    Utilità di supporto per l'applicazione principale.
    '''



    @staticmethod
    def get_stored_repositories():

        '''
        Restituisce la lista delle repository memorizzate come oggetto JSON. La
        lista è ottenuta da una risorsa esterna, che restituisce lo stesso
        oggetto JSON.

        :return: La lista delle repository memorizzate come oggetto JSON.
        '''

        json_url = os.environ.get('REPO')

        if json_url is None:
            return None
        
        response = requests.get(json_url)

        if response.status_code != 200:
            return None
        
        return json.loads(response.text)



    @staticmethod
    def assemble_repository(stored_repositories):

        '''
        Assembla le informazioni della repository con quelle aggiuntive ottenute
        dalle API di GitHub.

        :param repositoryInfo: contiene l'url della repository e l'autore.
        :return: Un oggetto Repository, contenente le informazioni della repository
                 e le informazioni aggiuntive ottenute dalle API di GitHub.
        '''

        repositories = [RepositoryInfo(**repository) for repository in stored_repositories]
        

        githubResponse = GithubResponse()

        for repo in repositories:

            githubResponse.call(repo)

            infos = githubResponse.get_infos()

            if infos is not None:
                repositories[repositories.index(repo)] = infos

        return repositories
