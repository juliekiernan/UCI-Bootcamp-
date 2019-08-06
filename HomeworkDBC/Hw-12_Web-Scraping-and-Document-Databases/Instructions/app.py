# import dependencies
from flask import Flask, render_template
import pymongo
from pymongo import MongoClient
import scrape_mars

# ceate flask app
app = Flask(__name__)

# create connection to mongo
client = pymongo.MongoClient('mongodb://localhost:27017/')

#create routes (home, scrape)
@app.route("/")
def index():
    mars = client.db.mars.find_one()
    return render_template ("index.html", mars = mars)

@app.route("/scrape")
def scrape():
    mars = client.db.mars
    mars_data = scrape_mars.scrape()
    mars.update({}, mars_data, upsert=True)
    return "whoo-hoo! It worked!!"

if __name__ == "__main__":
    # app.run()
    app.run(debug=True)

