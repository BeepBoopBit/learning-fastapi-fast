from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/page")
async def page01():
    return{"Page": "01"}

@app.post("/createpost")
async def create_post(payload: dict = Body(...)):
    print(payload)
    return{"Create": "Post"}


class Post(BaseModel):
    title: str
    content: str

@app.post("/createpost2")
async def create_post2(payload: Post):
    print(payload)
    return{"Create": "Post2"}