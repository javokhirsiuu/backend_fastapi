from schemas import Picture_name
from db import get_db
from fastapi import APIRouter,Depends,HTTPException,File
from moduls import UploadFile,Comment_Image


router = APIRouter()

@router.get("/all/picture")
async def all_picture(db=Depends(get_db)):
    all_picture_db = db.query(Comment_Image).all()
    return all_picture_db


@router.post("/upload/picture")
async def uploading_picture(name:Picture_name,file: UploadFile = File(...),db=Depends(get_db)):
    picture_save = db.query(Comment_Image).filter(Comment_Image.file_name == name).first()
    if picture_save is not None:
        raise HTTPException(status_code=404,detail=f"picture with this name {picture_save} already exists")
    else:
        picture_model = Comment_Image()
        picture_model.file_name = name
        db.add(picture_model)
        db.commit()
        return picture_model,{file.filename,"saved succesfuly"}

@router.delete("/delete --picture/")
async def delete_picture(id:int,db=Depends(get_db)):
    delete_picture_db = db.query(Comment_Image).filter(Comment_Image.id == id).first()
    if not delete_picture_db:
        raise HTTPException(status_code=404,detail="picture not found")
    db.delete(delete_picture_db)
    db.commit()
    return {"deleted succesfully"}

