# main.py
# 


import json
import os
import time
import logging
from config import configure
from data.pr_check import check_pr
from create import create_template

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

print("---")
print("LAT-python")
logging.info("Application started")

# Create template files if they do not exist

create_template()

# Load configuration file if not yet configured: language is being configured

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

if not config["configured"]:
    language = input("Please enter your language (en, de): ")
    if language not in ["en", "de"]:
        print("Invalid language. Defaulting to English (en).")
        language = "en"
    configure(language)

# Load configuration file and update language settings

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)
language = config["language"]

json_path = os.path.join("lang", f"{language}.json")

with open(json_path, "r", encoding="utf-8") as f:
    texts = json.load(f)

time.sleep(2)

# greeting

print(texts["greeting"])
print()
time.sleep(1)
print("---")
print()

# Start of the main loop

while True:
    print(texts["main_menu"])
    print(texts["main_option_1"])
    print(texts["main_option_2"])
    print(texts["main_option_3"])
    print(texts["main_option_end"])
    main_selection = int(input(texts["main_input"]))
    
    print()
    print("---")
    print()

    if main_selection == 0:
        break
    elif main_selection == 1:
        pass
    elif main_selection == 2:
        with open("data/values.json") as f:
            values = json.load(f)
    
        disciplines = [entry["discipline"] for entry in values]
        print(texts["add_values_greeting"])
        print()
        print(texts["choose_discipline_documented"])
        print(*disciplines, sep=", ")
        print()
        print(texts["add_values_documented"])
        print(texts["add_values_new"])
        add_values_selection = int(input(texts["add_values_input"]))
        if add_values_selection == 1:
            pass
        elif add_values_selection == 2:
            pass
        else:
            pass
    elif main_selection == 3:
        pass
    else:
        print(texts["invalid_main_input"])

logging.info("Application terminated")