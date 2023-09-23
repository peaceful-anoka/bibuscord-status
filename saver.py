import json


# Function to get user input
def get_user_input():
    name = input("Enter your name: ")
    button1_url = input("Button1 URL:")
    button2_url = input("Button2 URL:")
    button1_label = input("Button1 label:")
    button2_label = input("Button2 label:")

    user_info = {
        "name": name,
        "button1_url": button1_url,
        "button2_url": button2_url,
        "button1_label": button1_label,
        "button2_label": button2_label
    }

    return user_info


# Function to save user input to a JSON file
def save_to_json(user_info, filename):
    with open(filename, 'w') as json_file:
        json.dump(user_info, json_file, indent=4)


if __name__ == "__main__":
    user_info = get_user_input()
    filename = "save.json"
    save_to_json(user_info, filename)
    print(f"User information has been saved to {filename}")
