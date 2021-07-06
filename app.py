from flask import Flask, render_template, redirect
from dotenv import load_dotenv
from os import environ
from flask_pymongo import PyMongo
import ScrapedRandomRollerCoaster

load_dotenv()

app = Flask(__name__)
app.config['MONGODB_URI'] = environ.get('MONGODB_URI')

#database set-up
mongo = PyMongo(app, uri=

@app.route("/")
def home():
    random_coaster = mongo.db.random_coaster.find_one()
    return render_template("index.html", random_data=random_coaster)

@app.route("/scrape")
def scrape():
    random_data = ScrapedRandomRollerCoaster.scrape()
    mongo.db.random_coaster.update({}, random_data, upsert=True)

@app.route('/api/coasters/mongo')
def coasters_mongo():
    coasters = mongo.db.rc_db.find()
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