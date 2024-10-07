from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, status
import uvicorn
from .secret import authentication
from .database import get_db,engine
from harlequelrah_fastapi.authentication.token import Token,AccessToken,RefreshToken
from fastapi.security import OAuth2PasswordRequestForm

User=authentication.User
UserLoginModel=authentication.User


app = FastAPI()
async def get_current_user():
    await authentication.get_current_user()


# models.Base.metadata.create_all(bind=engine)

AUTHENTICATION_EXCEPTION = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid email/username or password",
    headers={"WWW-Authenticate": "Beaer"},
)


@app.post("/tokenUrl", response_model=Token)
async def login_api_user(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = await authentication.authenticate_user(
        db, form_data.username, form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email/username or password",
            headers={"WWW-Authenticate": "Beaer"},
        )
    data = {"sub": form_data.username}
    access_token = authentication.create_access_token(data)
    refresh_token = authentication.create_refresh_token(data)

    return {
        "access_token": access_token["access_token"],
        "refresh_token": refresh_token["refresh_token"],
        "token_type": "bearer",
    }


@app.get("/refresh-token", response_model=AccessToken)
async def refresh_token(refresh_token: RefreshToken):
    access_token = authentication.refresh_token(refresh_token)
    return access_token


@app.get("/refresh-token", response_model=AccessToken)
async def refresh_token(current_user: User = Depends(authentication.get_current_user)):
    data = {"sub": current_user.username}
    access_token = authentication.create_access_token(data)
    return access_token


@app.post("/login", response_model=Token)
async def login(usermodel: UserLoginModel, db: Session = Depends(get_db)):
    if (usermodel.email is None) ^ (usermodel.username is None):
        credential = usermodel.username if usermodel.username else usermodel.email
        user = await authentication.authenticate_user(db, credential, usermodel.password)
        if not user:
            raise AUTHENTICATION_EXCEPTION
        data = {"sub": credential}
        access_token = authentication.create_access_token(data)
        refresh_token = authentication.create_refresh_token(data)
        return {
            "access_token": access_token["access_token"],
            "refresh_token": refresh_token["refresh_token"],
            "token_type": "bearer",
        }
    else:
        raise AUTHENTICATION_EXCEPTION


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
