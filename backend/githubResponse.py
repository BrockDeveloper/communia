import os
import requests
from datetime import datetime
from models.repository import Repository
from models.repositoryInfo import RepositoryInfo


BASE_GIT_URL = "https://github.com/"
BASE_API_URL = "https://api.github.com/repos/"


class GithubResponse:

    '''
    This class is used to get the informations of a repository from the Github API.
    '''


    def __init__(self, repositoryInfo: RepositoryInfo):

        self.repositoryInfo = repositoryInfo
        self.apicall = BASE_API_URL + repositoryInfo.url.replace(BASE_GIT_URL, "")

        self.response = self.__call__()


    
    def __call__(self):

        '''
        This method is used to call the Github API.
        
        :return: The response of the API as a JSON object.
        '''

        try:

            headers = {"Authorization": "token " + os.environ.get("TOKEN")}

            response = requests.get(self.apicall, headers=headers)
            return response.json()
        
        except Exception:
            return None
    


    def get_infos(self):

        '''
        This method is used to get the informations of a repository from the Github API.
        
        :return: A Repository object.
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