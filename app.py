from flask import Flask, render_template, request,jsonify, url_for
import os
import pickle
import plotly.express as px
import pandas as pd

app = Flask(__name__)

picfolder = os.path.join("static","images")




import numpy as np

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))
app.config["UPLOAD_FOLDER"] = picfolder
@app.route("/")
def home():

    return render_template("homepage.html")



@app.route("/predict", methods = ["GET",'POST'])
def mypredict():
    myTemperature = int(request.form.get("Temperature", False))
    myPrecipitation	= int(request.form.get("Precipitation", False))
    myExport	= int(request.form.get("Export", False))
    myFertilizer = int(request.form.get("Fertilizer", False))	
    myAvocados = int(request.form.get("Avocados", False))	
    myBananas = int(request.form.get("Bananas", False))	
    myRice	 = int(request.form.get("Rice", False)) 	
    myWheat	= int(request.form.get("Wheat", False))
   
    print([myTemperature,myPrecipitation,myExport,myFertilizer,myAvocados,myBananas,myRice,myWheat ])
    myfin = np.array([[myTemperature,myPrecipitation,myExport,myFertilizer,myAvocados,myBananas,myRice,myWheat ]])
    prediction = model.predict(myfin)
    return render_template("predict.html", my_ourbeans=f"{prediction[0]}")



if  __name__ == "__main__":
    app.run(debug=True)     