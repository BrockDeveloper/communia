from pydantic import BaseModel


class RepositoryInfo(BaseModel):

    '''
    Rappresenta le informazioni essenziali di una repository, autore e url
    che consente di ottenere le informazioni complete sulla repository.
    '''


    url: str
    author: str