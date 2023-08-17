from fastapi import FastAPI
from user_router import router as user_router
from comment_router import router as comment_router

app = FastAPI()

app.include_router(user_router)
app.include_router(comment_router)









