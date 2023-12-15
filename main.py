from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Endpoint is up!!"}


@app.get("/me")
async def me():
    return {"message": "This endpoint is about my handle @plusminuschirag go find me on linkedin and github"}
