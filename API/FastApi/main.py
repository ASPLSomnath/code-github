from fastapi import FastAPI,Body
from pydantic import BaseModel
# somnath
app = FastAPI()

class Post(BaseModel):
    title: str
    content: str 
    publised: bool = True
    ratting: int = None


@app.get('/info')
def info():
    info = {
        'name': 'somnath chakrborty',
        'gmail': "som@gmail.com",
        'work': 'devloper',
    }
    return info


@app.post("/bodyPost")
def new_post(post_using_body = Body(...)):
    print(post_using_body)
    return {"data": "post_using_body"}

@app.post("/pydenticPost")
def new_post(postUsingPydenticAndClass : Post):
    print(postUsingPydenticAndClass)
    return {"data": "post_Using_Pydentic_And_Class"}


# @app.get("/bro")
# def root():
#     return 'Hey Bro'

# @app.get("/")
# def hello():
#     return "Hello"

# @app.get("/bye")
# def bye():
#     return "Bye"