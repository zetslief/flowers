from flask import Flask, render_template, jsonify
import csv

app = Flask(__name__, instance_relative_config=True)

CONFIG_FILE_NAME = 'config.py'
app.config.from_pyfile(CONFIG_FILE_NAME)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/flowers')
def get_flowers():
    flowers = []
    with open('flower_data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            flowers.append({'name': row[0], 'image_path': row[1]})
    return jsonify(flowers)

if __name__ == '__main__':
    port = app.config['PORT'] if 'PORT' in app.config else 5000
    app.run(host='localhost', port=9874)
