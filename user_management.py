from utils import load_config

def login():
    config = load_config()
    password = input("Enter password: ")
    return password == config["password"]

def reset_password(new_password):
    config = load_config()
    config["password"] = new_password
    save_config(config)
