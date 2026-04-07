import json

def configure(language):
    with open("config.json", "r", encoding="utf-8") as f:
        configure = json.load(f)
    configure["configured"] = True
    configure["language"] = language

    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(configure, f)

