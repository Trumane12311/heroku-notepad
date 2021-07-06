from flask import Flask, render_template, redirect
from dotenv import load_dotenv
from os import environ
from flask_pymongo import PyMongo

load_dotenv()

app = Flask(__name__)
app.config['MONGODB_URI'] = environ.get('MONGODB_URI')

#database set-up
mongo = PyMongo(app)

@app.route("/")
def home():
    return 'Roller Coaster Database API'

@app.route('/api/coasters/mongo')
def coasters_mongo():
    coasters = mongo.rc_db.coasters.find()
    data = []

    for coaster in coasters:
        data.append({
          '_id': str(coaster['_id']),
          'Roller Coaster': str(coaster['Roller Coaster']),
          'Amusement Park': str(coaster['Amusement Park']),
          'Type': str(coaster['Type']),
          'Design': str(coaster['Design']),
          'Opened': datetime(coaster['Opened'])
        })

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)