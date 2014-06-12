from app import app, db
import os
from datetime import datetime

class Antoine(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    formula = db.Column(db.String(160), unique = True)
    name = db.Column(db.String(140))
    A = db.Column(db.String(20))
    B = db.Column(db.String(20))
    C = db.Column(db.String(20))
    Tmin = db.Column(db.String(20))
    Tmax = db.Column(db.String(20))
    Punit = db.Column(db.String(20))
    Tunit = db.Column(db.String(20))
    Source = db.Column(db.String(160))

    def __init__(self, formula, name, A, B, C, Tmin, Tmax, Tunit = 'degC', Punit = 'mmHg', Source = ''):
        self.formula = formula
        self.name = name
        self.A = A
        self.B = B
        self.C = C
        self.Tmin = Tmin
        self.Tmax = Tmax
        self.Tunit = Tunit
        self.Punit = Punit
        self.Source = Source

def create():
    import pandas as pd
    from pandas import DataFrame as df

    filename = app.config['DOWNLOADS'] + "/antoine_data.csv"

    data = pd.read_csv(filename)

    for index, row in data.iterrows():
        antoine = Antoine(formula = row.Formula,
            name = row['Compound Name'],
            A = row.A,
            B = row.B,
            C = row.C,
            Tmin = row.TMIN,
            Tmax = row.TMAX,
            Source = 'Knovel')

        db.session.add(antoine)

    db.session.commit()

    return filename