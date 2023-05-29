import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
import yfinance as yf

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
    'units': [50, 100, 150],
    'epochs': [20, 30, 40],
    'batch_size': [32, 64, 128]
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
    return best_params

# Perform tuning and training
def perform_tuning_and_training():
    global search_method

    search_method = search_method_var.get()

    # Perform hyperparameter tuning
    best_params = perform_hyperparameter_tuning(X_train, y_train)
    print("Best hyperparameters:", best_params)

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

    # Plot the results
    plt.plot(data['Close'], color='blue', label='Actual')
    plt.plot(np.concatenate([train_predictions, test_predictions]), color='red', label='Predicted')
    plt.title('Nvidia Stock Price Prediction')
    plt.xlabel('Time')
    plt.ylabel('Stock Price')
    plt.legend()
    plt.show()

# Import Tkinter for GUI
from tkinter import *
from tkinter import ttk

# Create the main window
root = Tk()
root.title("Stock Price Prediction")
root.geometry("300x150")

# Variable to store the selected search method
search_method_var = StringVar()
search_method_var.set("grid")

# Function to update the search method
def update_search_method():
    print("Search Method:", search_method_var.get())

# GridSearchCV button
grid_button = Radiobutton(root, text="GridSearchCV", variable=search_method_var, value="grid", command=update_search_method)
grid_button.pack()

# RandomizedSearchCV button
random_button = Radiobutton(root, text="RandomizedSearchCV", variable=search_method_var, value="random", command=update_search_method)
random_button.pack()

# Perform tuning and training button
train_button = Button(root, text="Perform Tuning and Training", command=perform_tuning_and_training)
train_button.pack()

# Run the main loop
root.mainloop()