from flask import render_template, flash, redirect, url_for, request, g
from app import app, db
from datetime import datetime
from sqlalchemy import desc
import os.path

@app.route('/')
@app.route('/index')
def index():
    meta = 'Thermodynamic chemistry databases that are easy to search, read, and use!'
    return render_template('index.html',
        meta_description = meta)