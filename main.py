from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/page")
async def page01():
    return{"Page": "01"}

@app.post("/createpost")
async def create_post():
    return{"Create": "Post"}