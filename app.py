from flask import Flask, render_template, request,jsonify, url_for
import os
import pickle
import pandas as pd
import numpy as np
import plotly_express as px 


#this is the code that locate where our image files are 
picfolder = os.path.join("static","images")

#we are initialing the Flask app
app = Flask(__name__)

# this is the code that open the model.pkl file where we save our predict values and model
model = pickle.load(open("model.pkl", "rb"))
app.config["UPLOAD_FOLDER"] = picfolder


#this code link to homepage in our templates folder
@app.route("/")
def home():

    return render_template("homepage.html")






#this code link to visulisation.html page in our templates folder

@app.route('/visulisation')
def visulisation():
    df = pd.read_csv("Data/crop_yield_data.csv")
    # Create your Plotly Express visualization
    fig = px.bar(df, x='Year', y='Export Quantity')

    # Convert the figure to JSON
    graphJSON = fig.to_json()

    fig2 = px.bar(df, x='Yield', y='Crop')
    graphJSON2 = fig2.to_json()


    # Render the HTML template with the graphJSON
    return render_template('visulisation.html', graphJSON=graphJSON, graphJSON2=graphJSON2)


#this code link to predict.html page  in our templates folder
# this is the same code that takes input values from the frontend and return the predict values
#in the predict.html page

#we try to convert all the values to float because the parameter are float in data type and int as well

@app.route("/predict", methods = ['GET','POST'])
def mypredict():
    if request.method == 'POST':
        myTemperature = float(request.form.get("Temperature", False))
        myPrecipitation	= float(request.form.get("Precipitation", False))
        myExport	= float(request.form.get("Export", False))
        myFertilizer = float(request.form.get("Fertilizer", False))	
        myAvocados = int(request.form.get("Crop_Avocados", False))	
        myBananas = int(request.form.get("Crop_Bananas", False))	
        myRice	 = int(request.form.get("Crop_Rice", False)) 	
        myWheat	= int(request.form.get("Crop_Wheat", False))

        print([myTemperature,myPrecipitation,myExport,myFertilizer,myAvocados,myBananas,myRice,myWheat ])
        myfin = np.array([[myTemperature,myPrecipitation,myExport,myFertilizer,myAvocados,myBananas,myRice,myWheat ]])
        prediction = model.predict(myfin)
        if prediction[0]:
                my = prediction[0]
        else:
            my = " "

        return render_template("predict.html", my_ourbeans=f"{prediction[0]}")

    else:
        return render_template("predict.html", my_ourbeans=f" ")
         
         



if  __name__ == "__main__":
    app.run(debug=True)     