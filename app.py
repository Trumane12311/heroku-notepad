from flask import Flask, jsonify, render_template, redirect, request
from flask_pymongo import PyMongo
from os import environ
from dotenv import find_dotenv, load_dotenv
import ScrapedRandomRollerCoaster

app = Flask(__name__)
app.config['MONGO_URI'] = environ.get('MONGODB_URI', 'mongodb://localhost:27017/rc_DB')
mongo = PyMongo(app)

@app.route("/")
def home():
    random_coaster = mongo.db.random_coaster.find_one()
    random_data = ScrapedRandomRollerCoaster.scrape()
    mongo.db.random_coaster.update({}, random_data, upsert=True)
    return render_template("index.html", random_data=random_coaster)
    #return 'Welcome to my API'

@app.route("/api/coasters/")
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
        data.append(coaster_info)
    return jsonify(data)

@app.route("/api/records/drop")
def drops_mongo():
    drops = mongo.db.drop_records.find({})
    drop_data = []

    for drop in drops:
        coaster_info = ({
            '_id': str(drop['_id']),
            'latitude': drop['latitude'],
            'longitude': drop['longitude'],
            'geometry': drop['geometry'],
            'City': drop['City'],
            'Rank': drop['Rank'],
            'Drop': drop['Drop'],
            'Roller Coaster': drop['Roller Coaster'],
            'Amusement Park': drop['Amusement Park'],
            'State': drop['State'],
            'Country': drop['Country']
            })
        drop_data.append(coaster_info)
    return jsonify(drop_data)

@app.route("/api/records/height")
def heights_mongo():
    heights = mongo.db.height_records.find({})
    height_data = []

    for height in heights:
        coaster_info = ({
            '_id': str(height['_id']),
            'latitude': height['latitude'],
            'longitude': height['longitude'],
            'geometry': height['geometry'],
            'City': height['City'],
            'Rank': height['Rank'],
            'Height': height['Height'],
            'Roller Coaster': height['Roller Coaster'],
            'Amusement Park': height['Amusement Park'],
            'State': height['State'],
            'Country': height['Country']
            })
        height_data.append(coaster_info)
    return jsonify(height_data)

@app.route("/api/records/length")
def lengths_mongo():
    lengths = mongo.db.length_records.find({})
    length_data = []

    for length in lengths:
        coaster_info = ({
            '_id': str(length['_id']),
            'latitude': length['latitude'],
            'longitude': length['longitude'],
            'geometry': length['geometry'],
            'City': length['City'],
            'Rank': length['Rank'],
            'Length': length['Length'],
            'Roller Coaster': length['Roller Coaster'],
            'Amusement Park': length['Amusement Park'],
            'State': length['State'],
            'Country': length['Country']
            })
        length_data.append(coaster_info)
    return jsonify(length_data)

@app.route("/api/records/speed")
def speeds_mongo():
    speeds = mongo.db.speed_records.find({})
    speed_data = []

    for speed in speeds:
        coaster_info = ({
            '_id': str(speed['_id']),
            'latitude': speed['latitude'],
            'longitude': speed['longitude'],
            'geometry': speed['geometry'],
            'City': speed['City'],
            'Rank': speed['Rank'],
            'Speed': speed['Speed'],
            'Roller Coaster': speed['Roller Coaster'],
            'Amusement Park': speed['Amusement Park'],
            'State': speed['State'],
            'Country': speed['Country']
            })
        speed_data.append(coaster_info)
    return jsonify(speed_data)

if __name__ == "__main__":
    app.run(debug=True)