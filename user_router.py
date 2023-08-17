from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_db, engine, Base
from moduls import User

from schemas import User_schema,edit_user

Base.metadata.create_all(bind=engine)

router = APIRouter(tags=["users"],
                   prefix="/user")


@router.get("/all-users")
async def read_users(db: Session = Depends(get_db)):
    query = db.query(User).all()
    return query
@router.get("get-user")
async def read_user(user_id:int,db: Session = Depends(get_db)):
    user_get = db.query(User).filter(User.id == user_id).first()
    if not user_get:
        raise HTTPException(status_code=404,detail="not found")
    else:
        db.refresh(user_get)
        db.commit()
    return user_get


@router.post("/add-user")
async def create_user(user: User_schema,
                      db: Session = Depends(get_db)):
    user_model = User()
    user_model.username = user.username
    user_model.password = user.password
    user_model.email = user.email

    db.add(user_model)
    db.commit()
    return user_model
@router.put("/update/user")
async def update_user(id:int,updated:edit_user,db:Session = Depends(get_db)):
    updater_user =db.query(User).filter(User.id == id).first()
    if not updater_user:
        raise HTTPException(status_code=404,detail="try again")

    updated_model = User()
    updated_model.username = updated.username_updated
    updated_model.password = updated.password_updated
    updated_model.email = updated.email_updated
    db.add(updated_model)
    db.delete(updater_user)
    db.commit()
    return updated_model




@router.delete("/delete-comment")
async def delete_user(user_id: int, db=Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return "User deleted successfully"
