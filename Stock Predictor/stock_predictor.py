import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
import yfinance as yf
from gui import StockPredictionGUI

# Define the stock symbol and time range
stock_symbol = "NVDA"
start_date = "2010-01-01"
end_date = "2023-07-01"

# Extract historical stock price data from Yahoo Finance
data = yf.download(stock_symbol, start=start_date, end=end_date)

# Prepare the data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1, 1))

# Split the data into training and testing sets
train_size = int(len(scaled_data) * 0.8)
train_data = scaled_data[:train_size]
test_data = scaled_data[train_size:]

# Create sequences of input data
def create_sequences(data, seq_length):
    X = []
    y = []
    for i in range(len(data) - seq_length):
        X.append(data[i:i + seq_length])
        y.append(data[i + seq_length])
    return np.array(X), np.array(y)

seq_length = 10
X_train, y_train = create_sequences(train_data, seq_length)
X_test, y_test = create_sequences(test_data, seq_length)

# Build the LSTM model
def build_model(units=50):
    model = Sequential()
    model.add(LSTM(units=units, return_sequences=True, input_shape=(seq_length, 1)))
    model.add(LSTM(units=units))
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# Wrap the Keras model inside the scikit-learn wrapper
regressor = KerasRegressor(build_fn=build_model)

# Define the hyperparameter search space
param_grid = {
    'units': [50, 100],
    'epochs': [20, 30],
    'batch_size': [32, 64]
}

# Define the search method
search_method = None

# Function to perform hyperparameter tuning
def perform_hyperparameter_tuning(X, y):
    global search_method

    if search_method == 'grid':
        search = GridSearchCV(estimator=regressor, param_grid=param_grid, cv=3)
    elif search_method == 'random':
        search = RandomizedSearchCV(estimator=regressor, param_distributions=param_grid, cv=3)
    else:
        print("Invalid search method selected.")
        return

    search.fit(X, y)
    best_params = search.best_params_
    best_score = search.best_score_
    print("Best hyperparameters:", best_params)
    print("Best score:", best_score)
    return best_params, best_score

# Perform tuning and training
def perform_tuning_and_training():
    global search_method

    search_method = gui.search_method_var.get()

    # Perform hyperparameter tuning
    best_params, best_score = perform_hyperparameter_tuning(X_train, y_train)

    # Build the model with the best hyperparameters
    model = build_model(units=best_params['units'])

    # Train the model
    model.fit(X_train, y_train, epochs=best_params['epochs'], batch_size=best_params['batch_size'])

    # Evaluate the model
    train_predictions = model.predict(X_train)
    test_predictions = model.predict(X_test)

    # Inverse transform the predictions to get actual stock prices
    train_predictions = scaler.inverse_transform(train_predictions)
    test_predictions = scaler.inverse_transform(test_predictions)

    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

    # Plot the actual stock prices
    ax1.plot(data.index, data['Close'], color='blue', label='Actual')
    ax1.set_title('Actual Nvidia Stock Prices')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Stock Price')
    ax1.legend()

    # Plot the predicted stock prices
    ax2.plot(data.index[train_size + seq_length:], test_predictions, color='red', label='Predicted')
    ax2.set_title('Predicted Nvidia Stock Prices')
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Stock Price')
    ax2.legend()

    # Adjust the layout and display the figure
    plt.tight_layout()
    plt.show()


gui = StockPredictionGUI()
gui.run()
