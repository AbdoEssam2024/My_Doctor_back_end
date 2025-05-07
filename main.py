from fastapi import FastAPI
from controller.user_controller import login

app = FastAPI()


@app.get("/")
def home():
    return {"msg": "Hello from Railway!"}


@app.post("/login")
async def userLogin(username: str, password: str):
    return await login(username, password)
