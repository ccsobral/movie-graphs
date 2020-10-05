from flask import Blueprint, jsonify, request
from api.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/search', methods=('POST',))
def search():
    db = get_db()

    text_input = request.json['input']
    
    results = db.execute(
        'SELECT b.id, b.title' 
        ' FROM basics b INNER JOIN ratings r on b.id = r.id'
        ' WHERE LOWER(b.title) LIKE ?'
        ' ORDER BY r.avgRating * r.numVotes DESC',
        ('%' + text_input + '%',)
        ).fetchmany(10)

    return {'data': results}

#Simple hello page
@bp.route('/hello')
def hello():
    return 'Hello, World!'