from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from fastapi.exceptions import HTTPException
from passlib.context import CryptContext
from jose import jwt
import os
from dotenv import load_dotenv
from fastapi.responses import RedirectResponse

# Cargar variables de entorno
load_dotenv()

app = FastAPI(docs_url="/login/custom-docs", redoc_url="/login/custom-redoc", openapi_url="/login/openapi.json")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Configuración
SECRET_KEY = os.getenv("SECRET_KEY", "a0b2c3d4e5f67890123456789abcdef")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Contexto de criptografía
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Usuarios
users = {
    "edgar": {"username": "edgar", "email":"edgar@mail.com", "password": pwd_context.hash("ed123")},
    "diego": {"username": "diego", "email":"diego@mail.com", "password": pwd_context.hash("diego123")},
    "jerly": {"username": "jerly", "email":"jerly@mail.com", "password": pwd_context.hash("jerly123")},
}
              
# Funciones
def encode_token(payload: dict) -> str:
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def decode_token(token: Annotated[str, Depends(oauth2_scheme)]) -> dict:
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user = users.get(data["username"])
        if user is None:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


@app.post("/login/token")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = users.get(form_data.username)
    if user is None or not pwd_context.verify(form_data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    token = encode_token({"username": user["username"], "email": user["email"]})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/login/users/profile")
def profile(my_user: Annotated[dict, Depends(decode_token)]):
    return my_user

@app.get("/login")
def main():
    return RedirectResponse(url="/login/custom-docs")