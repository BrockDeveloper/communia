from pydantic import BaseModel


class RepositoryInfo(BaseModel):

    '''
    This class is used to store the repository baseinformation.
    '''

    url: str
    author: str