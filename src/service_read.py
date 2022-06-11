from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"description": "read service"}

@app.get("/read/{npm}")
async def read(npm: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_npm(db, npm)
    # asumsi pasti ada
    return {
        'status':'OK',
        'npm':db_user.npm,
        'nama':db_user.nama
    }


