import os
import requests
from datetime import datetime
from models.repository import Repository
from models.repositoryInfo import RepositoryInfo


BASE_GIT_URL = "https://github.com/"
BASE_API_URL = "https://api.github.com/repos/"


class GithubResponse:

    '''
    Richiama le API di GitHub ed elabora le informazioni sulle repository.
    '''


    def __init__(self):
            
        self.repositoryInfo = None
        self.apicall = None
        self.response = None

    

    def call(self, repositoryInfo: RepositoryInfo):

        '''
        Richiama le API di GitHub su una specifica repository e, se la risposta
        è positiva, ne ottiene le informazioni.

        :param repositoryInfo: contiene l'url della repository e l'autore.
        :return: None
        '''

        self.repositoryInfo = repositoryInfo
        self.apicall = BASE_API_URL + repositoryInfo.url.replace(BASE_GIT_URL, "")

        self.response = self.__call__()


    
    def __call__(self):

        '''
        Richiama le API di GitHub.

        :return: La risposta delle API, in formato JSON.
        '''

        try:

            headers = {"Authorization": "token " + os.environ.get("TOKEN")}

            response = requests.get(self.apicall, headers=headers)

            if response.status_code != 200:
                return None
            
            return response.json()
        
        except Exception:
            return None
    


    def get_infos(self):

        '''
        Restituisce le informazioni della repository.

        :return: Un oggetto Repository, contenente le informazioni della repository
                 e le informazioni aggiuntive ottenute dalle API di GitHub.
        '''

        if not self.response:
            return None
        
        repository = Repository(
            
            **self.repositoryInfo.dict(),

            stars = int(self.response.get("stargazers_count")),

            created = int(datetime.strptime(self.response.get("created_at"), 
                                            "%Y-%m-%dT%H:%M:%SZ").year),

            updated = int(datetime.strptime(self.response.get("updated_at"), 
                                            "%Y-%m-%dT%H:%M:%SZ").year)
        )

        return repository
