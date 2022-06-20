from flask import request, Blueprint
from faker import Faker

import requests
import json
import csv

fake_elements = Faker()


bp = Blueprint('hw2', __name__)


@bp.route("/requirements/")
def requirements():
    value = []
    with open('requirements.txt') as csv_file:
        a = csv_file.readlines()
        for i in a:
            value.append(f'<p>{i}<p>')
    return ''.join(value)


@bp.route("/generate-users/")
def generator():
    arg_from_get = request.args.get('count', default=100)
    email_lst = []
    for i in range(int(arg_from_get)):
        email_lst.append(f'Email: {fake_elements.ascii_free_email()}, Name: {fake_elements.name()}')
    return '<br>'.join(email_lst)


@bp.route("/mean/")
def height_weight():
    height = []
    weight = []
    with open('hw.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        for row in reader:
            height.append(float(row[' "Height(Inches)"']) * 2.54)
            weight.append(float(row[' "Weight(Pounds)"']) * 0.453592)
    return f'<p>Average Height: {round(sum(height) / len(height), 2)}<p>' \
           f'<p>Average Weight: {round(sum(weight) / len(height), 2)}<p>'


@bp.route("/space/")
def space():
    try:
        get_request = requests.get('http://api.open-notify.org/astros.json')
        if get_request.status_code != 200:
            return '<p>API request unsuccessful.<p>'
        else:
            dict_exchanges = json.loads(get_request.content)
            number = dict_exchanges['number']
            return f'<p>In space now {number} astronauts.<p>'
    except requests.exceptions.ConnectionError:
        return '<p>No internet connection!<p>'
