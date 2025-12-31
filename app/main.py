from fastapi import FastAPI , Request
from app.database import engine ,Base
from fastapi.responses import JSONResponse
from app.models import User, Post , Like ,Followers , Comment
from app.routes import user
from app.utils.jwt_handler import decode_access_token


app = FastAPI()

Base.metadata.create_all(bind = engine)

# JWT middleware
@app.middleware("http")
async def jwt_auth_middleware(request: Request, call_next):
    # Public routes that should skip authentication
    public_paths = ["/password","/post/search","/user/login", "/user/register", "/docs", "/openapi.json"]

    # Allow public routes
    if any(request.url.path.startswith(path) for path in public_paths):
        return await call_next(request)

    # Check Authorization header
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return JSONResponse(status_code=401, content={"detail": "Authorization token missing"})

    token = auth_header.split(" ")[1]
    payload = decode_access_token(token)
    if not payload:
        return JSONResponse(status_code=401, content={"detail": "Invalid or expired token"})

    # Store user info in request.state for later use in routes
    request.state.user = payload

    # Continue to the route
    return await call_next(request)

app.include_router(user.router, prefix="/user", tags=["User"])