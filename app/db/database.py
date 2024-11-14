from pymongo import MongoClient

from app.settings.mongo_config import DB_URL

client  = MongoClient(DB_URL)

db = client['emails']
all_emails = db['all_emails']
# ordered_collection = db['ordered']

