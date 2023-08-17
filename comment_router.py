from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import db
from db import get_db
from moduls import COMMENTS, User
from schemas import COOMMENT_schemas,comment_send,ONLY_COMMENTS

router = APIRouter(tags=["comment"],
                   prefix="/comment")


@router.get("/all/comment")
async def read_comment(db: Session = Depends(get_db)):
    query1 = db.query(COMMENTS).all()
    return query1

@router.get("/comment/{id}")
async def get_comment(COMMENT_ID: int,
                      db: Session = Depends(get_db)):
    query = db.query(COMMENTS).filter(COMMENTS.id == COMMENT_ID).first()

    if not query:
        raise HTTPException(status_code=404,detail="tupoymisan")

    return query


@router.post("/add-comment")
async def create_comment(comment:comment_send, db: Session = Depends(get_db)):
    create_comment = COMMENTS()
    db.add(create_comment)

    db.commit()
    return create_comment,"sended succesfully"




@router.put("/edit/comment/")
async def edit_comment(comment_id: int,updated:COOMMENT_schemas,db=Depends(get_db)):
    updater_comment = db.query(COMMENTS).filter(COMMENTS.id == comment_id).all()
    if not updater_comment:
        raise HTTPException(status_code=404, detail="try again")

    else:
        updated_model = COMMENTS()
        updated_model.comments = updated.updated
        db.add(updated_model)
        db.commit()
        return updated_model



@router.delete("/delete-comment")
async def delete_comment(comment_id: int, db=Depends(get_db)):
    comment = db.query(COMMENTS).filter(COMMENTS.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="comment not found")
    db.delete(comment)
    db.commit()
    return "comment deleted successfully"
