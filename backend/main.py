from fastapi import FastAPI
from fastapi.responses import Response
from githubResponse import GithubResponse
import json
from models.repository import Repository
from models.repositoryInfo import RepositoryInfo


app = FastAPI()


@app.middleware("http")
async def add_cors_header(request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


@app.get("/")
def root():

    repositories: Repository = []

    with open("assets/repositories.json", "r") as file:
        
        loaded_repositories = json.load(file)

        for repository in loaded_repositories:
                
            repositoryInfo = RepositoryInfo(**repository)
            repositories.append(repositoryInfo)


    for repo in repositories:

        response = GithubResponse(repo)
        infos = response.get_infos()

        repositories[repositories.index(repo)] = infos

    return repositories