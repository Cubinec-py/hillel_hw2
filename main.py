from flask import Flask

import csv

app = Flask(__name__)


@app.route("/requirements/")
def requirements():
    value = []
    with open('requirements.txt', 'r', newline='') as csv_file:
        a = csv.reader(csv_file, delimiter=' ')
        for i in a:
            value.append(', '.join(i))
    return '<p>\n<p>'.join(value)


if __name__ == '__main__':
    app.run()