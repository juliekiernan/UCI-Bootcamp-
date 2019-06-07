from flask import flask, jsonify

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import numpy as np
import pandas as pd


engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

app = Flask(__name__)

@app.route("/")
def home():
    print("Server received request for home page")
    return(
        f"Homepage for Hawaiian Climate Analysis"<br/>
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<starts>/<end><br/>"
        )

@app.route("/api/v1.0/precipitation")   
def precipitation():
    return jsonify (precipitation):

@app.route("/api/v1.0/stations")   
def stations():
    return jsonify (num_stations):

@app.route("/api/v1.0/tobs")   
def tobs():
    return jsonify (tobs):

@app.route("/api/v1.0/<start>")   
def start_date():
    return jsonify (start_date):

@app.route("/api/v1.0/<starts>/<end>")   
def end_date():
    return jsonify (end_date):

if __name__ == "main":
    app.run(debug=True)