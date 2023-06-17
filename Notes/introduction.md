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

