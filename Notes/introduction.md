# Getting started with FastAPI

First install it by doing the following commands:

```
apt-get install uvicorn
pip install "fastapi[all]"
```

after than, test it by creating a `main.py` file containing the following code:

```py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return{"message": "Hello, Word"}

```

then run it using the following command:

```
uvicorn main:app
```

If everything is working, let's continue with the learning

## Learning the basic syntax

If we want to route a url to a function, we need to put `@<appname>.<method>('<url>')`. Just like what we did on our first example

```py
@app.get("/")
async def root():
    return{"message", "Hello, world"}
```

Let's try to create more routes

```py
@app.get("/")
async def root():
    return{"message", "Hello, world"}

@app.get("/page")
async def page01():
    return{"Page": "01"}

```

## Using Thunder client for testing

Just a note that you can use thunder client for testing easier. Just install it as an extention in your vscode. No sign-in requried


## Creating a post request

This is quite easy in FastAPI. Just change the method and you're good to go. Kind of like this:

```py
@app.post("/somePost")
async def do_post(){
    return{"Message":"The post has been done"}
}
```
### Accepting data

Of course, when we want to do post, we want to also accept data from it. In order for us to do it, we need to put some parameters

```py
from fastapi.params import Body
@app.post("/newPost")
async def do_data_psot(payload: dic = Body(...)):
    print(payload)
    return {"STATUS CODE: SUCCESSFUL"}
```

### Accepting data with a model

In this case, we want to make use of pydantic, so better install it using `pip install pydantic`. If you already installed it, we just need to create a class that inheritcs the `BaseModel` from the module, and pass it as a parameter

```py
from pydantic import BaseModel

class Post:
    title: str
    content: str

@app.post("/newPost2")
async def do_new_post(payload: Post):
    print(payload)
    return("CONFIRMATION":"YES")

```

### Accepting data with better model

We can also create optional and default values. However, in order to do the opinional fields, we need to import `Optional` from `typing`:

```py
class BetterPost(BaseModel):
    title:str
    content:str
    published:bool = False
    rating: Optional[int] = None
    
@app.post("/createpost3")
async def create_post3(payload: BetterPost):
    print(payload)
    return{"Create": "Post3"}
```