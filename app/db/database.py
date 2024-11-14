from pymongo import MongoClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.settings.mongo_config import DB_URL
from app.settings.sql_config import SQL_DB_URL

client  = MongoClient(DB_URL)

db = client['emails']
all_emails = db['all_emails']
# ordered_collection = db['ordered']


def init_db():
    all_emails.drop()


engine = create_engine(SQL_DB_URL)
session_maker = sessionmaker(bind=engine)

