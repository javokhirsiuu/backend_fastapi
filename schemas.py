from pydantic import BaseModel

class COOMMENT_ID(BaseModel):
    comment_only_id:int

class comment_send(BaseModel):
    comment_id:int
    comment:str
    user_id:int

class COMMENTS_SCHEMAS_read(BaseModel):
    id: int
    commment: str



class User_schema(BaseModel):
    username: str
    email: str
    password: str



class USER_SCHEMAS_READ(BaseModel):
    user_id: int
    email: str
    username: str
    id: int




class USER_DELETE(BaseModel):
    id: int

class EDITING_COMMENT(BaseModel):
    comment_editing:str

class COOMMENT_schemas(BaseModel):
    comment_id: int
    updated:str


class ONLY_COMMENTS(BaseModel):
    comments:str

class edit_user(BaseModel):
    email_updated: str
    username_updated: str
    password_updated:str