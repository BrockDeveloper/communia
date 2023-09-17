from models.repositoryInfo import RepositoryInfo


class Repository(RepositoryInfo):

    '''
    Rappresenta una repository con tutte le informazioni disponibili,
    ovvero quelle essenziali e quelle ottenute dalle api di github.
    '''


    stars: int
    created: int
    updated: int