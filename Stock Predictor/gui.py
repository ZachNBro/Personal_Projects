from tkinter import *
from tkinter import ttk

class StockPredictionGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Stock Price Prediction")
        self.root.geometry("300x150")

        # Variable to store the selected search method
        self.search_method_var = StringVar()
        self.search_method_var.set("grid")

        # GridSearchCV button
        self.grid_button = Radiobutton(self.root, text="GridSearchCV", variable=self.search_method_var, value="grid")
        self.grid_button.pack()

        # RandomizedSearchCV button
        self.random_button = Radiobutton(self.root, text="RandomizedSearchCV", variable=self.search_method_var, value="random")
        self.random_button.pack()

        # Perform tuning and training button
        self.train_button = Button(self.root, text="Perform Tuning and Training", command=self.perform_tuning_and_training)
        self.train_button.pack()

    def perform_tuning_and_training(self):
        # Import the required functions from main.py
        from stock_predictor import perform_tuning_and_training

        # Call the function from main.py
        perform_tuning_and_training()

    def run(self):
        # Run the main loop
        self.root.mainloop()