import json

def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)

def save_config(data):
    with open('config.json', 'w') as f:
        json.dump(data, f, indent=4)
