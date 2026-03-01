from flask import Flask, request,jsonify,render_template 
import joblib
import pandas as pd

# Load trained model
rf_model = joblib.load("rf_model.pkl")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    hour = data["hour"]
    line_id = data["line_id"]
    stop_id = data["stop_id"]

    input_df = pd.DataFrame([{
        "hour": hour,
        "line_id": line_id,
        "stop_id": stop_id
    }])

    predicted_passengers = rf_model.predict(input_df)[0]

    OVER_CROWD_LIMIT = 20
    verdict = "Overcrowded" if predicted_passengers >= OVER_CROWD_LIMIT else "Not Overcrowded"

    return jsonify({
        "predicted_passengers": float(predicted_passengers),
        "verdict": verdict
    })

if __name__ == "__main__":
    app.run(debug=True)