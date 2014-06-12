from flask import render_template, flash, redirect, url_for, request, g, abort
from app import app, db
from datetime import datetime
from sqlalchemy import desc
import os.path
from models import Antoine

@app.route('/')
@app.route('/index')
def index():
    meta = 'Thermodynamic chemistry databases that are easy to search, read, and use!'
    return render_template('index.html',
        meta_description = meta)

@app.route('/db/<db_name>/')
def db(db_name = None):
    meta = "Database of thermodynamic properties."
    if db_name is None:
        flash('Sorry. That database does not exist yet.', 'error')
        return redirect( url_for('index') )

    # retrieve the database by db_name
    if db_name == 'Antoine':
        try:
            db = Antoine.query.order_by('formula').all()
        except:
            flash("Error getting information from database", 'error')
            return redirect( url_for('index') )

    else:
        return abort(404)

    return render_template('db.html',
        db = db,
        meta_description = meta)