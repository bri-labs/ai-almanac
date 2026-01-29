# Load trained model and expose API using Flask
from flask import Flask, request, jsonify
import pandas as pd
import joblib

app=Flask(__name__)

# Load trained model
model=joblib.load("iris_model.pkl")

# Routes
@app.route("/")
def home():
    return "Welcome to the IRIS Classifier API"

@app.route("/predict", methods=["POST"])
def predict():
    data=request.get_json() #Expect JSON with parameters
    df=pd.DataFrame([data])
    prediction=model.predict(df)[0]
    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

# Input
{
    "sepal"
}
