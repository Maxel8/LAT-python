import os
import shutil

def create_template():

    if not os.path.exists("config.json"):
        shutil.copy("templates/config.template.json", "config.json")
    if not os.path.exists("data/pr.json"):
        shutil.copy("templates/pr.template.json", "data/pr.json")
    if not os.path.exists("data/values.json"):
        shutil.copy("templates/values.template.json", "data/values.json")
    if not os.path.exists("app.log"):
        shutil.copy("templates/app.template.log", "app.log")