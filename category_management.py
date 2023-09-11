from utils import load_config, save_config

def add_category(category_type, category_name):
    config = load_config()
    if category_type == "income":
        config["income_categories"].append(category_name)
    elif category_type == "expense":
        config["expense_categories"].append(category_name)
    save_config(config)

def remove_category(category_type, category_name):
    config = load_config()
    if category_type == "income":
        config["income_categories"].remove(category_name)
    elif category_type == "expense":
        config["expense_categories"].remove(category_name)
    save_config(config)
