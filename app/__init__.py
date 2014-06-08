from flask import Flask
import os
from config import basedir, ADMINS
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.moment import Moment
from flaskext.markdown import Markdown

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
moment = Moment(app)
Markdown(app)

from app import views, models

if __name__ == "__main__":
    app.run()