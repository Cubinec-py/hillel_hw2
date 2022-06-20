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
