import json


# Function to load data from the JSON file
def load_from_json(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data


# Specify the filename where the data is stored
filename = "save.json"
# Load the data from the JSON file
user_info = load_from_json(filename)

# Access specific information
name = user_info["name"]
button1_url = user_info["button1_url"]
button2_url = user_info["button2_url"]
button1_label = user_info["button1_label"]
button2_label = user_info["button2_label"]
# Now you can use the 'name', 'age', and 'email' variables in your code
