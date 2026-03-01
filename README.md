# Public Transport Crowd Predictor 

A Machine Learning web application that predicts passenger crowd levels for public transport based on:

- Hour of the day
- Line ID
- Stop ID

## Project Overview

This project uses a Random Forest model trained on transport data to estimate expected passenger count.

The model is deployed using Flask and provides predictions via a simple web interface.

## 🛠 Tech Stack

- Python
- Flask
- Pandas
- Scikit-learn
- Joblib
- HTML/CSS

## How to Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Then open:

http://127.0.0.1:5000/

##  Project Structure

```
app.py
templates/
    index.html
rf_model.pkl
requirements.txt
.gitignore
```

## Future Improvements

- Add better UI styling
- Deploy on Render
- Add data visualization dashboard
- Add input validation
