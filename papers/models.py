#from django.db import models

from django.conf import settings
from couchdb import Server
from couchdb.mapping import Document, TextField

# set up connection to couchdb in code
SERVER = Server(getattr(settings, 'COUCHDB_SERVER', 'http://127.0.0.1:5984'))
if ('papers' not in SERVER):
    SERVER.create('papers')


# Create your models here.

class Paper(Document):
    title = TextField()
    abstract = TextField()
    type = TextField()
