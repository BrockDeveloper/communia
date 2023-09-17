import uvicorn
from fastapi import FastAPI
from workers.util import Util
from fastapi.responses import Response


'''
Istanza dell'applicazione FastAPI
'''
app = FastAPI()



@app.middleware("http")
async def add_cors_header(request, call_next):

    '''
    Consente di aggiungere l'header "Access-Control-Allow-Origin" alla risposta
    di ogni richiesta HTTP, ovvero consente di effettuare richieste da un
    dominio diverso da quello del server.
    '''

    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"

    return response



@app.get("/")
def root():

    '''
    Unica route dell'applicazione, restituisce la lista delle repository con
    tutte le informazioni disponibili per ognuna di esse.
    '''

    stored_repositories = Util.get_stored_repositories()

    if stored_repositories is None:
        return Response(status_code=503)

    repositories = Util.assemble_repository(stored_repositories)

    if None in repositories:
        return Response(status_code=503)

    return repositories



if __name__ == "__main__":
    
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=False)