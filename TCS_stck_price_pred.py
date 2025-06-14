
from flask import Flask, request, render_template
import pickle
import numpy as np

# Load trained model
with open('tcs_rf_best_model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract 10 features matching the model's training features
        input_features = ['Open', 'High', 'Low', 'Close', 'Volume', 
                          'Returns', 'MA5', 'MA10', 'MA20', 'Volatility']

        features = [float(request.form[f]) for f in input_features]
        
        # Predict
        prediction = model.predict([features])[0]
        
        return render_template('index.html', prediction_text=f'Predicted Close Price: ₹{prediction:.2f}')
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)


