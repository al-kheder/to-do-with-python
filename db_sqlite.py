# db_sqlite.py

import os
from flask_sqlalchemy import SQLAlchemy

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
DATABASE = os.path.join(PROJECT_ROOT, 'todo.db')

def get_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + DATABASE
    return SQLAlchemy(app)


class Todo:
    def __init__(self, db):
        self.db = db
        self.todo = type('Todo', (db.Model,), {
            'id': db.Column(db.Integer, primary_key=True),
            'title': db.Column(db.String(80)),
            'complete': db.Column(db.Boolean)
        })
