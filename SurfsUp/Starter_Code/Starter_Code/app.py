# Import the dependencies.
import pandas as pd
import numpy as np
import datetime as dt
import sqlalchemy 
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify



#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(autoload_with=engine)


Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

app = Flask(__name__)


# reflect an existing database into a new model
@app.route("/")
def welcome():
    return (f"Welcome to Our Newe Page <br/>"
           
           f" Here is Our Routes <br/>"
           
           f"/api/v1.0/precipitation <br/>"
           
           f"/api/v1.0/stations <br/>"
           
           f"/api/v1.0/tobs <br/>"

           f"/api/v1.0/start_end")
           
# reflect the tables
date = dt.datetime(2016,8,23)
@app.route("/api/v1.0/precipitation")

def precipitation():
   date_prcp = session.query(Measurement.prcp , Measurement.date).\
    filter(Measurement.date >= date).\
    order_by(Measurement.date).all()
   date_prcp_dictionary = {date : x for date , x in date_prcp}
   return jsonify(date_prcp_dictionary)


@app.route("/api/v1.0/stations")

def station():
    json_station = session.query(Station.station).all()
    list_station = list(np.ravel(json_station))
    return jsonify (list_station)



@app.route("/api/v1.0/tobs")

def tobs():
    date_temp_active = session.query(Measurement.tobs).\
            filter(Measurement.station == 'USC00519281' ).\
            filter(Measurement.date >= '2017,8,23').all()
    list_date_temp = list(np.ravel(date_temp_active ))
    return jsonify (list_date_temp)



@app.route ("/api/v1.0/start_end")

def temps(start,end):
    start_end = session.query(Measurement).filter(Measurement.date>= start).filter(Measurement.date<=end)
    list_of_temp =[] 
    for row in start_end :
        list_of_temp.append(row.tobs) 
    return (jsonify ({"Minimum Temperature is ": min(list_of_temp ),"Maximum Temperature is ": max(list_of_temp ),"Average Temperature is ":np.mean}))
           
            

if __name__ == "__main__":
   app.run(port=3000,debug=True)

# Save references to each table


# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################




#################################################
# Flask Routes
#################################################
