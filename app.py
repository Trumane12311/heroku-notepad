from flask import Flask, jsonify, render_template, redirect
from dotenv import load_dotenv
from flask_pymongo import PyMongo
from os import environ
from datetime import datetime
#from dotenv import find_dotenv, load_dotenv
import ScrapedRandomRollerCoaster

s_user = environ.get('SEC_USERNAME')
s_pass = environ.get('SEC_PASSWORD')

app = Flask(__name__)

#app.config['MONGO_URI'] = environ.get('MONGODB_URI')
mongo = PyMongo(app, uri=f'mongodb+srv://{s_user}:{s_pass}@cluster0.oxmmo.mongodb.net/rc_DB?retryWrites=true&w=majority')


@app.route("/")
def home():
    random_coaster = mongo.db.random_coaster.find_one()
    random_data = ScrapedRandomRollerCoaster.scrape()
    mongo.db.random_coaster.update({}, random_data, upsert=True)
    return render_template("index.html", random_data=random_coaster)

@app.route('/api/coasters/mongo')
def coasters_mongo():
    coasters = mongo.db.coasters.find({})
    data = []

    for coaster in coasters:
        coaster_info = ({
          '_id': str(coaster['_id']),
          'Roller Coaster': coaster['Roller Coaster'],
          'Amusement Park': coaster['Amusement Park'],
          'Type': coaster['Type'],
          'Design': coaster['Design']
        })
        data.append(coaster_info)

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)