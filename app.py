import scraping
import sys
from flask import Flask, render_template, redirect, url_for, jsonify
from flask_pymongo import PyMongo

### Importing the module needed for this project

app = Flask(__name__)

# Use flask_PyMongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongodb_client = PyMongo(app)
db = mongodb_client.db

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)
    #### rendeing the index page for the site

@app.route('/scrape')
def scrape():
    mars = scrape_mars.scrape()
    print("\n\n\n")

    db.mars_facts.insert_one(mars)
    return "Some scrapped data"
    
if __name__ == "__main__":
    app.run(debug=True)

