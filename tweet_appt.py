#import all the libraies needed to execute the following:
# - Launch flask
# - connect to mySQL database
# - Jsonify the mysql table
# SQL Alchemy
import os

from flask import (Flask, render_template, request, url_for,jsonify)


from flask_sqlalchemy import SQLAlchemy


# #Create an app
app = Flask(__name__)
# # The database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:dFtR4710*@localhost/trump_tweets'
db = SQLAlchemy(app)

#setting up the  Model that has exactly the same table properties in MYSQL table.
class Data(db.Model):
    __tablename__ = 'final_dataset'
    id = db.Column(db.Integer, primary_key=True) #<------ this is a must line to have even if the table does not have it
    Date = db.Column(db.Date, nullable=True)
    Open = db.Column(db.Float, nullable=True)
    High = db.Column(db.Float, nullable=True)
    Low = db.Column(db.Float, nullable=True)    
    Close = db.Column(db.Float , nullable=True)
    approve = db.Column(db.Float, nullable=True)
    disapprove = db.Column(db.Float, nullable=True)
    tweet = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return '<Data %r>' % self.Date


# Create database tables
# @app.before_first_request
def setup():
    # Recreate database each time for demo
    # db.drop_all()
    db.create_all()


#landing page
@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index.html")


# a testing page
@app.route("/about")
def about():
    print("PASS")
    return "This API is working"

# JSON object of all the tweets .
@app.route("/tweets")
def tweet():
    print("PASS")
    results = db.session.query(final_dataset.Date, final_dataset.tweet).all()

   

    trace = []
    for result in results:

        trace.append({
              "Date": result[0],
              "tweet": result[7]
        })
    return jsonify(trace)

# JSON object page of the approval, disapproval, and the open/close stock market
@app.route("/approval")
def apst():
    print("PASS")
    results = db.session.query(final_dataset.Date,final_dataset.disapproval,final_dataset.approval).all()

    trace = []
    for result in results:

        trace.append({
            "Date": result[0],
            "Approval": result[6],
            "Disapproval": result[5]
        })
    return jsonify(trace)

@app.route("/SPY")
def SPY():
    print("PASS")
    results = db.session.query(final_dataset.Open,final_dataset.High,final_dataset.Low,final_dataset.Close).all()

    trace = []
    for result in results:

        trace:append({
            "Date": result[0],
            "Open": result[1],
            "High": result[2],
            "Low": result[3,],
            "Close": result[4]
        })

    return jsonify(trace)


if __name__ == "__main__":
    app.run(debug=True)
