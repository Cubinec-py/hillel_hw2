from flask import Flask, request
from faker import Faker

import csv

app = Flask(__name__)
fake_elements = Faker()


@app.route("/requirements/")
def requirements():
    value = []
    with open('requirements.txt', 'r', newline='') as csv_file:
        a = csv.reader(csv_file, delimiter=' ')
        for i in a:
            value.append(', '.join(i))
    return '<p>\n<p>'.join(value)


@app.route("/generate-users/")
def generator():
    arg_from_get = request.args.get('count', '')
    email_lst = []
    for i in range(int(arg_from_get)):
        email_lst.append(f'{fake_elements.ascii_free_email()}')
    return '<p>\n<p>'.join(email_lst)


if __name__ == '__main__':
    app.run()
