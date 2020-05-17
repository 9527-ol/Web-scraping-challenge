from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)



@app.route("/")
def index():

    destination_data = mongo.db.mars.find_one() 

    return render_template("index.html", mars = destination_data)


@app.route("/scrape")
def scrape():
    
    mars_data = scrape_mars.scrape()
    mongo.db.mars.update({}, mars_data, upsert=True)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)


