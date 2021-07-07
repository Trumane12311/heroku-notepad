from flask import Flask, jsonify, render_template, redirect, request
from flask_pymongo import PyMongo
from os import environ
from dotenv import find_dotenv, load_dotenv
from selenium_chrome import Chrome
import ScrapedRandomRollerCoaster

app = Flask(__name__)
app.config['MONGO_URI'] = environ.get('MONGODB_URI', 'mongodb://localhost:27017/rc_DB')
mongo = PyMongo(app)

@app.route("/")
def home():
    #random_coaster = mongo.db.random_coaster.find_one()
    #random_data = ScrapedRandomRollerCoaster.scrape()
    #mongo.db.random_coaster.update({}, random_data, upsert=True)
    #return render_template("index.html", random_data=random_coaster)
    return 'Welcome to my API'

@app.route("/api/coasters")
def coasters_mongo():
    coasters = mongo.db.coasters.find({})
    data = []

    for coaster in coasters:
        coaster_info = ({
            '_id': str(coaster['_id']),
            'Roller Coaster': coaster['Roller Coaster'],
            'Amusement Park': coaster['Amusement Park'],
            'Type': coaster['Type'],
            'Design': coaster['Design'],
            'Status': coaster['Status'],
            'Opened': coaster['Opened']
            })
#        except KeyError:
            #coaster_info = ({
                #'_id': str(coaster['_id']),
                #'Roller Coaster': coaster['Roller Coaster'],
                #'Amusement Park': coaster['Amusement Park'],
                #'Type': coaster['Type'],
                #'Design': coaster['Design']
                 #})
 #       if coaster['Status'] is not None:
        data.append(coaster_info)
    return jsonify(data)

@app.route("/api/records/drop")
def coasters_mongo():
    drops = mongo.db.drop_records.find({})
    drop_data = []

    for drop in drops:
        coaster_info = ({
            '_id': str(coaster['_id']),
            'latitude': coaster['latitude'],
            'longitude': coaster['longitude'],
            'geometry': coaster['geometry'],
            'City': coaster['City'],
            'Rank': coaster['Rank'],
            'Drop': coaster['Drop'],
            'Roller Coaster': coaster['Roller Coaster'],
            'Amusement Park': coaster['Amusement Park'],
            'State': coaster['State'],
            'Country': coaster['Country']
            })
        drop_data.append(coaster_info)
    return jsonify(drop_data)

if __name__ == "__main__":
    app.run(debug=True)