from pydantic import BaseModel
from models.repositoryInfo import RepositoryInfo


class Repository(RepositoryInfo):

    '''
    This class is used to store the complete information of a repository.
    These informations are getted from the Github API.
    '''

    stars: int
    created: int
    updated: int