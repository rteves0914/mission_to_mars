from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars_collection = mongo.db.mars_collection.find_one()
    return render_template("index.html", mars_collection = mars_collection)


@app.route("/scrape")
def scraper():
    collection = mongo.db.mars_collection
    collection_data = scrape_mars.scrape()
    print(collection_data)
    collection.update({}, collection_data, upsert=True)
    return redirect("/")


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
