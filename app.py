from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle
import os

app = Flask(__name__)


def get_cleaned_data(form_data):
    gestation = float(form_data['gestation'])
    parity = int(form_data['parity'])
    age = float(form_data['age'])
    height = float(form_data['height'])
    weight = float(form_data['weight'])
    smoke = float(form_data['smoke'])

    cleaned_data = {"gestation":[gestation],
                    "parity":[parity],  
                    "age":[age],
                    "height":[height],
                    "weight":[weight],
                    "smoke":[smoke]
                    }


    return cleaned_data


@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")


EXCPECTED_COLUMNS = ["gestation","parity","age","height","weight","smoke"]

# define your endpoint
# def get_prediction is for post man
#@app.route("/predict", methods=['POST'])
#def get_prediction():
    # Get JSON data from request
    #data = request.get_json()

    # Clean data
   # baby_data_cleaned = get_cleaned_data(data)
   # baby_df = pd.DataFrame(baby_data_cleaned)

    # Load model
   # path = r"C:\Users\hp\OneDrive\Desktop\machine learning model\model.pkl"
   # with open(path, "rb") as obj:
      #  model = pickle.load(obj)

    # Predict
   # prediction = round(float(model.predict(baby_df)[0]), 2)

    # Return JSON response
   # return jsonify({"Prediction": prediction})

@app.route("/predict", methods=['POST'])
def get_prediction():
    # Get form data and clean it
    baby_data_cleaned = get_cleaned_data(request.form)
    baby_df = pd.DataFrame(baby_data_cleaned)

    # Load the trained model
    path = "model.pkl"
    with open(path, "rb") as obj:
        model = pickle.load(obj)

    # Make prediction
    prediction = round(float(model.predict(baby_df)[0]), 2)

    # Render result in template
    return render_template("index.html", prediction=prediction)

 
    





if __name__ == '__main__':
    app.run(debug=True)
# this for form in html
 #   @app.route("/predict", methods=['POST'])
#def get_prediction():
    # Get form data
   # baby_data_cleaned = get_cleaned_data(request.form)
 #   baby_df = pd.DataFrame(baby_data_cleaned)

    # Load model
  #  path = r"C:\Users\hp\OneDrive\Desktop\machine learning model\model.pkl"
   # with open(path, "rb") as obj:
  #      model = pickle.load(obj)

    # Predict
  #  prediction = round(float(model.predict(baby_df)[0]), 2)

    # Show in template
 #   return render_template("index.html", prediction=prediction)
