from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
import jwt
from datetime import datetime, timedelta

app = FastAPI()

# Secret key for JWT (in production, keep this secure and in environment variables)
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

# Simulated user database
fake_users_db = {
    "user@example.com": {
        "email": "user@example.com",
        "password": "password123"
    }
}

# Pydantic model for login request
class LoginRequest(BaseModel):
    email: str
    password: str

# Function to create JWT token
def create_jwt_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)  # Token expires in 30 minutes
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Function to verify JWT token
async def verify_token(authorization: Optional[str] = Header(default=None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token format")
    token = authorization.split("Bearer ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("email")
        if email is None or email not in fake_users_db:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"email": email}
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Login endpoint to generate JWT token
@app.post("/login")
async def login(request: LoginRequest):
    user = fake_users_db.get(request.email)
    if not user or user["password"] != request.password:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    # Create JWT token
    token_data = {"email": request.email}
    token = create_jwt_token(token_data)
    
    # Create response with token in Authorization header
    response = JSONResponse(content={"message": "Login successful"})
    response.headers["Authorization"] = f"Bearer {token}"
    return response

# Protected endpoint requiring token
@app.get("/protected")
async def protected_route(current_user: dict = Depends(verify_token)):
    return {"message": "This is a protected route", "user": current_user["email"]}

# Simple unprotected endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI JWT example"}