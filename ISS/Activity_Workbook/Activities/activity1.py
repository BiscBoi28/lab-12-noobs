'''
Task: Run the following code with the uvicorn server and hit the url on
the web
Command to be run on terminal: uvicorn activity1:app --reload
URL to be hit: http://127.0.0.1:8000/
'''

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read():
    return {"message": "my first fastapi server"}