from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# Serve a simple static HTML page
@app.get("/", response_class=HTMLResponse)
def read_root():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Home Page</title>
    </head>
    <body>
        <h1>Welcome to FastAPI!</h1>
        <p>This is a simple static HTML page served by FastAPI.</p>
        <a href="/about">Go to About Page</a>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

# Another static HTML page
@app.get("/about", response_class=HTMLResponse)
def about_page():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>About Page</title>
    </head>
    <body>
        <h1>About FastAPI</h1>
        <p>FastAPI is a modern, fast (high-performance), web framework for building APIs with Python.</p>
        <a href="/">Back to Home</a>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
