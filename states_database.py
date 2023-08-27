"""
    File name: states_database.py
    Author: Zachary Brown
    Python version: 3.9
    Description: A program that utilizes the dictionary
    data structure to store and pass states data.
"""
import sys
import urllib.request
import matplotlib.pyplot as plt
from PIL import Image
import json

with open('states.txt') as f:  # Open text file with state data
    data = f.read()

js = json.loads(data)  # convert data to JSON format


def menu():
    """Define menu options for user to choose from"""
    print("Welcome! Please make a selection: \n"
          "1. Display all U.S. States in Alphabetical order along with the Capital, State Population, and Flower \n"
          "2. Search for a specific state and display the appropriate Capital name, State Population, and an image of "
          "the associated State Flower. \n"
          "3. Provide a Bar graph of the top 5 populated States showing their overall population. \n"
          "4. Update the overall state population for a specific state. \n"
          "5. Exit Program")

    selection = input()
    if selection == "1":
        display(js)
    elif selection == "2":
        search(js)
    elif selection == "3":
        highest_population()
    elif selection == "4":
        set_population(js)
    elif selection == "5":
        # exit application
        print("Thank you for using this application!")
        sys.exit()
    else:
        print("Please enter a valid selection" + "\n")
        menu()


def display(js):
    """Define function to display all states in alphabetical order"""
    for state_name, (state_capital, population, state_flower, flower_url) in sorted(js.items()):
        print("State:", state_name, "Capital:", state_capital, "Population:", population, "Flower:", state_flower)
    menu()


def search(js):
    """Define function to search for specific state"""
    while True:
        state_search = input("Enter state to retreive data:")
        for state_name, (state_capital, population, state_flower, flower_url) in js.items():
            if state_name == state_search:
                print("State:", state_name, "Capital:", state_capital, "Population:", population, "Flower:",
                      state_flower)
                # open respective image of flower via URL
                try:

                    current_image = Image.open(urllib.request.urlopen(flower_url))
                    current_image.show()
                    menu()

                except:
                    print("Invalid URL")


def highest_population():
    """Define function to display plot of highest populated areas"""
    state_names = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania']
    population = [39_557_000, 28_701_800, 21_299_300, 19_542_200, 12_807_100, ]

    plt.figure(figsize=(10, 10))
    plt.xlabel("State Name")
    plt.ylabel("Overall Population (Tens of Millions)")
    plt.suptitle("Top 5 Highest Populated States")
    plt.bar(state_names, population)
    plt.show()
    menu()


def set_population(js):
    """Define function to change population"""
    while True:
        state_search = input("Enter a state to update its population:")
        for state_name, (state_capital, population, state_flower, flower_url) in js.items():
            if state_name == state_search:
                # enter new population value and set index position to new value
                new_population = int(input("Enter new population:"))
                if new_population > 0:
                    js[state_search][1] = new_population
                    menu()
                else:
                    print("Please enter a number that is positive")
                    continue


menu()