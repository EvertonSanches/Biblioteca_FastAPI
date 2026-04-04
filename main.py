from fastapi import FastAPI
from api.routes.leitor import router as leitor_router
from api.routes.livros import router as livro_router



app = FastAPI(title="Biblioteca_Digital")

@app.get("/")
def home():

    return {"msg": "Bem-vindo à Biblioteca Digital!"}
app.include_router(leitor_router)
app.include_router(livro_router)