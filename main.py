from fastapi import FastAPI, Body

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World from Suleiman!!!!"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your post"}

@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    return {
        "new_post": {
            "title": payload['title'],
            "content": payload['content']
        }
    }