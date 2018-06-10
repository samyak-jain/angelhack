from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin

cred = credentials.Certificate("angelhack-123-firebase-adminsdk-8z2vi-44c0b91d8a.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
