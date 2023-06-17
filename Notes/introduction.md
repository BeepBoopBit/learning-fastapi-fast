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

##