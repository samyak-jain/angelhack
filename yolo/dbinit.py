from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
import env

client = Cloudant(env.username, env.password, url=env.url)
client.connect()

dbname = "location"

try:
    db = client.create_database(dbname)
except CloudantException:
    print('Database' + dbname + ' already exists!!')


if db.exists():
   print("'{0}' database exists.\n".format(dbname))
