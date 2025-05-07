from fastapi import FastAPI
from controller.user_controller import login

app = FastAPI()


@app.post("/login")
async def userLogin(username: str, password: str):
    return await login(username, password)
