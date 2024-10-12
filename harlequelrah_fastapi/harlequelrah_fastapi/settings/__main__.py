from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, status
import uvicorn
from .secret import authentication
from .database import engine



app = FastAPI()



# models.Base.metadata.create_all(bind=engine)





if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
