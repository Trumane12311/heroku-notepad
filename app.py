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

@app.route("/index.html")
def index():
    random_coaster = mongo.db.random_coaster.find_one()
    random_data = ScrapedRandomRollerCoaster.scrape()
    mongo.db.random_coaster.update({}, random_data, upsert=True)
    return render_template("index.html", random_data=random_coaster)

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/international.html")
def international():
    return render_template("international.html")

@app.route("/chartist.html")
def chartist():
    return render_template("chartist.html")

@app.route("/multiplots.html")
def multiplots():
    return render_template("multiplots.html")

@app.route("/recordholders.html")
def recordholders():
    return render_template("recordholders.html")

@app.route("/glossary.html")
def glossary():
    return render_template("glossary.html")

@app.route("/API.html")
def api():
    return render_template("API.html")

@app.route("/api/coasters/")
def coasters_mongo():
    coasters = mongo.db.coasters_json.find_one({})
    coasters['_id'] = str(coasters['_id'])
    return jsonify(coasters)

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

@app.route("/api/records/drop_geo")
def drops_geo_mongo():
    drops = mongo.db.drop_records_geo.find_one({})
    drops['_id'] = str(drops['_id'])

    return jsonify(drops)

@app.route("/api/records/height_geo")
def heights_geo_mongo():
    heights = mongo.db.height_records_geo.find_one({})
    heights['_id'] = str(heights['_id'])

    return jsonify(heights)

@app.route("/api/records/length_geo")
def lengths_geo_mongo():
    lengths = mongo.db.length_records_geo.find_one({})
    lengths['_id'] = str(lengths['_id'])

    return jsonify(lengths)

@app.route("/api/records/speed_geo")
def speeds_geo_mongo():
    speeds = mongo.db.speed_records_geo.find_one({})
    speeds['_id'] = str(speeds['_id'])

    return jsonify(speeds)

@app.route("/api/worldview")
def world_geo_mongo():
    world = mongo.db.worldview.find_one({})
    world['_id'] = str(world['_id'])

    return jsonify(world)

@app.route("/api/coasters/csv")
def coasters_csv():
    coasters = mongo.db.coasters_csv.find({})
    coaster_data = []

    for coaster in coasters:
        coaster_info = ({
            '_id': str(coaster['_id']),
            'RollerCoaster': coaster['RollerCoaster'],
            'AmusementPark': coaster['AmusementPark'],
            'Type': coaster['Type'],
            'Design': coaster['Design'],
            'Status': coaster['Status'],
            'Opened': coaster['Opened']
            })
        
        coaster_data.append(coaster_info)

    return jsonify(coaster_data)

if __name__ == "__main__":
    app.run(debug=True)