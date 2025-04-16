from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# note the directory structure of static
app.mount("/static", StaticFiles(directory="static"), name="static")

# note the directory structure of templates
templates = Jinja2Templates(directory="templates")

@app.get("/variables")
async def show_variables(request: Request):
    context = {"request": request, "name": "Aaditya", "age": 22}
    return templates.TemplateResponse("variables.html", context)

@app.get("/if-else")
async def show_if_else(request: Request):
    context = {"request": request, "score": 75}
    return templates.TemplateResponse("if_else.html", context)

@app.get("/for-loop")
async def show_for_loop(request: Request):
    context = {"request": request, "items": ["Apple", "Banana", "Orange"]}
    return templates.TemplateResponse("for_loop.html", context)

@app.get("/comments")
async def show_comments(request: Request):
    return templates.TemplateResponse("comments.html", {"request": request})

@app.get("/inheritance")
async def show_inheritance(request: Request):
    return templates.TemplateResponse("inheritance.html", {"request": request})

@app.get("/css")
async def show_css(request: Request):
    return templates.TemplateResponse("css_example.html", {"request": request})

@app.get("/css-js")
async def show_css_js(request: Request):
    return templates.TemplateResponse("css_js_example.html", {"request": request})
