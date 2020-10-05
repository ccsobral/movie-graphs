import sqlite3
import re

from flask import current_app, g

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

def regexp(y, x, search=re.search):
    return 1 if search(y, x) else 0

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = make_dicts
        g.db.create_function('regexp', 2, regexp)
    
    return g.db