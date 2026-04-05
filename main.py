import json
import os
import time
from config import configure

print("---")
print("LAT-python")

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

if not config["configured"]:
    language = input("Please enter your language (en, de): ")
    if language not in ["en", "de"]:
        print("Invalid language. Defaulting to English (en).")
        language = "en"
    configure(language)

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)
language = config["language"]

json_path = os.path.join("lang", f"{language}.json")

with open(json_path, "r", encoding="utf-8") as f:
    texts = json.load(f)

time.sleep(2)

print(texts["greeting"])
print()
time.sleep(1)
print("---")
print()
while True:
    break