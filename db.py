
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine





engine = create_engine("postgresql://postgres:java2103@localhost:5432/Twitter")
Session_LOCAL = sessionmaker(autoflush=False,autocommit=False,bind=engine)
Base = declarative_base()




def get_db():
    global db
    try:
        db = Session_LOCAL()
        yield db
    finally:
        db.close()



