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


def menu():
    """Define menu options for user to choose from"""
    print("Welcome! Please make a selection: \n" \
          "1. Display all U.S. States in Alphabetical order along with the Capital, State Population, and Flower \n" \
          "2. Search for a specific state and display the appropriate Capital name, State Population, and an image of the associated State Flower. \n" \
          "3. Provide a Bar graph of the top 5 populated States showing their overall population. \n" \
          "4. Update the overall state population for a specific state. \n" \
          "5. Exit Program")

    selection = input()
    if selection == "1":
        display()
    elif selection == "2":
        search()
    elif selection == "3":
        highest_population()
    elif selection == "4":
        set_population()
    elif selection == "5":
        # exit application
        print("Thank you for using this application!")
        sys.exit()
    else:
        print("Please enter a valid selection" + "\n")
        menu()


states = {"Alabama": ["Montgomery", 4_887_870, "Camellia",
                      "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/camellia-flower.jpg"],
          "Alaska": ["Juneau", 737_438, "Forget-Me-Not",
                     "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/Alpineforgetmenot.jpg"],
          "Arizona": ["Phoenix", 7_171_650, "Suguaro Catus Blossom",
                      "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/saguaroflowersFlickr.jpg"],
          "Arkansas": ["Little Rock", 3_013_820, "Apple Blossom",
                       "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/AppletreeblossomArkansasflower.jpg"],
          "California": ["Sacremento", 39_557_000, "California Poppy",
                         "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/CAflowerCaliforniaPoppy.jpg"],
          "Colorado": ["Denver", 5_695_560, "White and Lavender Columbine",
                       "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/Colorado_columbine2.jpg"],
          "Connecticut": ["Hartford", 3_572_660, "Mountain Laurel",
                          "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/Mountain-Laural-flowers2.jpg"],
          "Florida": ["Tallahassee", 21_299_300, "Orange Blossom",
                      "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/OrangeBlossomsFloridaFlower.jpg"],
          "Georgia": ["Atlanta", 10_519_500, "Cherokee Rose",
                      "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/CherokeeRoseFlower.jpg"],
          "Hawaii": ["Honolulu", 1_420_490, "Pua Aloalo",
                     "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/yellowhibiscusPuaAloalo.jpg"],
          "Idaho": ["Boise", 1_754_210, "Syringa",
                    "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/syringaPhiladelphuslewisiiflower.jpg"],
          "Illinois": ["Springfield", 12_741_100, "Purple Violet",
                       "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/singlebluevioletflower.jpg"],
          "Indiana": ["Indianaplois", 6_691_880, "Peony",
                      "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/PeonyPaeoniaflowers.jpg"],
          "Iowa": ["Des Moines", 3_156_140, "Wild Prairie Rose",
                   "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/WildPrairieRose.jpg"],
          "Kansas": ["Topeka", 2_911_500, "Sunflower",
                     "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/native-sunflowers.jpg"],
          "Kentucky": ["Frankfort", 4_468_400, "Goldenrod",
                       "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/stateflowergoldenrod-bloom.jpg"],
          "Louisiana": ["Baton Rouge", 4_659_980, "Magnolia",
                        "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/MagnoliagrandifloraMagnoliaflower.jpg"],
          "Maine": ["Augusta", 1_338_400, "White Pine Cone & Tassel",
                    "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/whitepinemalecones.jpg"],
          "Tennessee": ["Nashville", 6_770_010, "Iris",
                        "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/LouisianaIrisWildflower-0.jpg"],
          "Maryland": ["Annapolis", 6_042_720, "Black-eyed Susan",
                       "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/FlowerMDBlack-eyedSusan.jpg"],
          "Deleware": ["Dover", 967_171, "Peach Blossom",
                       "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/peachblossomspeachflowers.jpg"],
          "Massachusettes": ["Boston", 6_902_150, "Mayflower",
                             "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/MayflowerTrailingArbutus.jpg"],
          "Rhode Island": ["Providence", 1_057_320, "Violet",
                           "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/violetsflowers.jpg"],
          "Minnesota": ["St.Paul", 5_611_180, "Pink and White Lady-Slipper",
                        "statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/pinkwhiteladysslipperflower1.jpg"],
          "Mississippi": ["Jackson", 2_986_530, "Magnolia",
                          "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/magnoliablossomflower01.jpg"],
          "Missouri": ["Jefferson City", 6_126_450, "White Hawthorn Blossom",
                       "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/hawthornflowersblossoms1.jpg"],
          "Michigan": ["Lansing", 9_995_920, "Apple Blossom",
                       "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/appleblossombeauty.jpg"],
          "Montana": ["Helena", 1_062_300, "Bitterroot",
                      "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/bitterrootfloweremblem.jpg"],
          "Nebraska": ["Lincoln", 1_929_270, "Goldenrod",
                       "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/goldenrodflowersyellow4.jpg"],
          "Nevada": ["Carson City", 3_034_390, "Sagebrush",
                     "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/Nevada-Sagebrush-Artemisia-tridentata.jpg"],
          "New Hampshire": ["Concord", 1_356_460, "Purple Lilac",
                            "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/lilacflowerspurplelilac.jpg"],
          "Vermont": ["Montpelier", 626_299, "Red Clover",
                      "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/redcloverstateflowerWV.jpg"],
          "New Jersey": ["Trenton", 8_908_520, "Violet",
                         "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/singlebluevioletflower.jpg"],
          "New Mexico": ["Santa Fe", 2_095_430, "Yucca",
                         "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/YuccaFlowersclose.jpg"],
          "New York": ["Albany", 19_542_200, "Rose",
                       "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/redrosebeautystateflowerNY.jpg"],
          "North Carolina": ["Raleigh", 10_383_600, "Dogwood",
                             "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/floweringdogwoodflowers2.jpg"],
          "Wyoming": ["Cheyenne", 577_737, "Indian Paintbrush",
                      "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/indianpaintbrushWYflower.jpg"],
          "North Dakota": ["Bismark", 760_077, "Wild Prairie Rose",
                           "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/flowerwildprairierose.jpg"],
          "Ohio": ["Columbus", 11_689_400, "Scalet Carnation",
                   "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/redcarnationOhioflower.jpg"],
          "Oklahoma": ["Oklahoma City", 3_943_080, "Mistletoe",
                       "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/mistletoe_phoradendron_serotinum.jpg"],
          "Oregon": ["Salem", 4_190_710, "Oregon Grape",
                     "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/Oregongrapeflowers2.jpg"],
          "Pennsylvania": ["Harrisburg", 12_807_100, "Mountain Laurel",
                           "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/Mt_Laurel_Kalmia_Latifolia.jpg"],
          "South Carolina": ["Columbia", 5_084_130, "Yellow Jessamine",
                             "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/CarolinaYellowJessamine101.jpg"],
          "South Dakota": ["Pierre", 882_235, "Pasque Flower",
                           "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/Pasqueflower-03.jpg"],
          "Texas": ["Austin", 28_701_800, "Bluebonnet",
                    "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/BluebonnetsBlueRed.jpg"],
          "Utah": ["Salt Lake City", 3_161_100, "Sego Lily",
                   "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/SegoLily.jpg"],
          "Virginia": ["Richmond", 8_517_680, "Dogwood",
                       "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/floweringdogwoodflowers2.jpg"],
          "Washington": ["Olympia", 7_535_590, "Pink Rhododendron",
                         "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/flower_rhododendronWeb.jpg"],
          "West Virginia": ["Charleston", 1_805_830, "Rhododendron",
                            "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/rhododendronWVstateflower.jpg"],
          "Wisconsin": ["Madison", 5_813_570, "Wood Violet",
                        "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/wood-violet.jpg"]
          }


def display():
    """Define function to display all states in alphabetical order"""
    for state_name, (state_capital, population, state_flower, flower_url) in sorted(states.items()):
        print("State:", state_name, "Capital:", state_capital, "Population:", population, "Flower:", state_flower)
    menu()


def search():
    """Define function to search for specific state"""
    while True:
        state_search = input("Enter state to retreive data:")
        for state_name, (state_capital, population, state_flower, flower_url) in states.items():
            if state_name == state_search:
                print("State:", state_name, "Capital:", state_capital, "Population:", population, "Flower:",
                      state_flower)
                # open respective image of flower via URL
                try:

                    current_image = Image.open(urllib.request.urlopen("http://" + flower_url))
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


def set_population():
    """Define function to change population"""
    while True:
        state_search = input("Enter a state to update its population:")
        for state_name, (state_capital, population, state_flower, flower_url) in states.items():
            if state_name == state_search:
                # enter new population value and set index position to new value
                new_population = int(input("Enter new population:"))
                if new_population > 0:
                    states[state_search][1] = new_population
                    menu()
                else:
                    print("Please enter a number that is positive")
                    continue

menu()
