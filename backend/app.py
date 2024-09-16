from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"msg": "Hello World"}

@app.get("/main")
async def root():
    return {"msg": "My World"}