# import datetime as dt
# import numpy as np
# import pandas as pd

# import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#set-up connection to database 
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create session (link) to the DB
session = Session(engine)

#set-up flask
app = Flask(__name__)

#all available flask routes
@app.route("/")
def home():
    return(
        f"Homepage for Hawaiian Climate Analysi\n"
        f"Available Routes:\n"
        f"/api/v1.0/precipitation\n"
        f"/api/v1.0/stations\n"
        f"/api/v1.0/tobs\n"
        f"/api/v1.0/<start\n"
        f"/api/v1.0/<starts>\n"
        )

# convert query results to dictionary using date as the key, and prcp as the value
@app.route("/api/v1.0/precipitation")   
def precipitation():
    prior_yr = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prior_yr).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# return  json list of stations
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    station = list(np.ravel(results))
    return jsonify(station)

# query for dates & temps from a year from the last data point; return json list of temps for that period
@app.route("/api/v1.0/tobs")
def tobs():
    prior_yr = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date >= prior_yr).all()
    temp = list(np.ravel(results))
    return jsonify (temp)

# return a josn list of temp min, max and averge for given start date () or end date ()
# when given the start only, calculate tmin, tvg, and tmax for all date greater than or equal to start date
# when given the start AND end date, calculate same for date between the start AND end date (inclusive)
@app.route("/api/v1.0/<start>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    if not end:
        # calculate TMIN, TAVG, TMAX for dates greater than start
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        # Unravel results into a 1D array and convert to a list
        temps = list(np.ravel(results))
        return jsonify(temps)

    # calculate TMIN, TAVG, TMAX with start and stop
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    # Unravel results into a 1D array and convert to a list
    temps = list(np.ravel(results))
    return jsonify(temps)

if __name__ == "__main__":
     app.run(debug=True)