from flask import Flask, jsonify, render_template, redirect
from flask_pymongo import PyMongo
#from os import environ
#from dotenv import find_dotenv, load_dotenv
#import ScrapedRandomRollerCoaster

app = Flask(__name__)
app.config['MONGO_URI'] = environ.get(
    'MONGO_URI')

#database set-up
mongo = PyMongo(app)

@app.route("/")
def home():
    return Welcome to Our Roller Coaster Database API!

#@app.route("/")
#def home():
    #random_coaster = mongo.db.random_coaster.find_one()
    #return render_template("index.html", random_data=random_coaster)

#@app.route("/scrape")
#def scrape():
    #random_data = ScrapedRandomRollerCoaster.scrape()
    #mongo.db.random_coaster.update({}, random_data, upsert=True)

@app.route('/api/coasters/mongo')
def coasters_mongo():
    coasters = mongo.db.rc_DB.find()
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