from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin
import env

cred = credentials.Certificate("angelhack-123-firebase-adminsdk-8z2vi-44c0b91d8a.json")
firebase_admin.initialize_app(cred)

fb_db = firestore.client()

client = Cloudant(env.username, env.password, url=env.url)
client.connect()

dbname = "location"

try:
    db = client.create_database(dbname)
except CloudantException:
    print('Database' + dbname + ' already exists!!')


if db.exists():
   print("'{0}' database exists.\n".format(dbname))
