from flask import (
    Blueprint, render_template,
)
from flaskr.db import get_db

bp = Blueprint('hw3', __name__)


@bp.route('/names/')
def names():
    db = get_db()
    unique_names = db.execute(
        'SELECT COUNT ( DISTINCT artist ) as value FROM tracks;'
    ).fetchone()
    return render_template('html_sample/names.html', unique_names=unique_names)


@bp.route('/tracks/')
def tracks():
    db = get_db()
    tracks = db.execute(
        'SELECT COUNT ( id ) as value FROM tracks;'
    ).fetchone()
    return render_template('html_sample/tracks.html', tracks=tracks)


@bp.route('/tracks/<genre>')
def tracks_genre(genre):
    selected_genre = genre.lower()
    db = get_db()
    track_genre = db.execute(
        'SELECT COUNT( id ) as value FROM tracks WHERE tracks.genres = ?;', (selected_genre,)
    ).fetchone()
    return render_template('html_sample/trcaks_genre.html', track_genre=track_genre, selected_genre=selected_genre)