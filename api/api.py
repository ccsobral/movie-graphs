from flask import Blueprint, jsonify, request
from api.db import get_db
from api.plot_graph import plot_graph

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/search', methods=('POST',))
def search():
    db = get_db()

    text_input = request.json['input']
    
    results = db.execute(
        'SELECT b.id, b.title' 
        ' FROM basics b INNER JOIN ratings r on b.id = r.id'
        ' WHERE LOWER(b.title) LIKE ? AND b.type == ?'
        ' ORDER BY r.avgRating * r.numVotes DESC',
        ('%' + text_input + '%', 'tvSeries')
        ).fetchmany(10)

    return {'data': results}

@bp.route('/title/<string:title>')
def draw_plot(title):
    db = get_db()

    title_id = db.execute(
        'SELECT b.id'
        ' FROM basics b INNER JOIN ratings r on b.id = r.id'
        ' WHERE title == ?'
        ' ORDER BY r.avgRating * r.numVotes DESC',
        (title,)
    ).fetchone()['id']

    response = db.execute(
        'SELECT e.season as Season, '
        'RANK () OVER(ORDER BY e.season, e.episode) as Episodes, '
        'r.avgRating as Ratings, r.numVotes as Votes'
        ' FROM episodes e INNER JOIN ratings r on e.id = r.id'
        ' WHERE e.parent_id == ?'
        ' ORDER BY e.season, e.episode',
        (title_id,)
    ).fetchall()

    plot = plot_graph(response)
    return plot

#Simple hello page
@bp.route('/hello')
def hello():
    return 'Hello, World!'