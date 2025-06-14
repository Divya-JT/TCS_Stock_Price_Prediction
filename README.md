# TCS_Stock_Price_Prediction

# 📈 TCS Stock Price Prediction App

A machine learning project that predicts the closing price of Tata Consultancy Services (TCS) stock using historical stock data. The final model is served via a Flask web application with an interactive form for predictions.

---

## 📌 Features

- Random Forest Regression Model trained on historical TCS stock data
- Feature engineering (returns, moving averages, volatility, etc.)
- Exploratory Data Analysis with visualizations
- Hyperparameter tuning for better performance
- Flask-powered web UI for making predictions
- Model persistence using Pickle

---


📊 Input Features
The model expects 10 features as input:

Open

High

Low

Close

Volume

Returns

MA5 (5-day Moving Average)

MA10 (10-day Moving Average)

MA20 (20-day Moving Average)

Volatility

These are extracted or engineered from stock price data.

---

# 🚀 Future Improvements


Add LSTM/GRU models for time series prediction

Connect with a live API for real-time predictions

Deploy on cloud platforms like Heroku or Render
