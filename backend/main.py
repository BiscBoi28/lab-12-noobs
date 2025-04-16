from fastapi import FastAPI
from items import router as items_router
from analytics import router as analytics_router
from quiz import router as quiz_router
from users import router as users_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(items_router, prefix="/items")
app.include_router(analytics_router)
app.include_router(quiz_router)
app.include_router(users_router, prefix="/users")

# why the hell did I write this function?
@app.get("/home")
async def get_home():
    return {"message": "Welcome to the Multi-Page FastAPI App!"}