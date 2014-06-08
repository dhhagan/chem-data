from app import app, db
import os
from datetime import datetime

class Antoine(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    cas = db.Column(db.String(20), unique = True)
    name = db.Column(db.String(140))

    def __init__(self, cas, name):
        self.cas = cas
        self.name = name