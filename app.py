from flask import Flask, jsonify, render_template, redirect, request
from flask_pymongo import PyMongo
from os import environ
from dotenv import find_dotenv, load_dotenv
#from selenium_chrome import Chrome
#import ScrapedRandomRollerCoaster

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

@app.route("/api/coasters/mongo")
def coasters_mongo():
    coasters = mongo.db.coasters.find({})
    data = []

    for coaster in coasters[0:10]:
        try:
            coaster_info = ({
                '_id': str(coaster['_id']),
                'Roller Coaster': coaster['Roller Coaster'],
                'Amusement Park': coaster['Amusement Park'],
                'Type': coaster['Type'],
                'Design': coaster['Design'],
                'Opened': coaster['Opened']
                })
        except KeyError:
            coaster_info = ({
                '_id': str(coaster['_id']),
                'Roller Coaster': coaster['Roller Coaster'],
                'Amusement Park': coaster['Amusement Park'],
                'Type': coaster['Type'],
                'Design': coaster['Design']
                 })
 #       if coaster['Status'] is not None:
        data.append(coaster_info)
        print(coaster.keys())
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)