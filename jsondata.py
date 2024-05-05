import json

# Define the JSON file path
file_path = "data\\friends.json"

def add_friend(new_friend_name):
    data = {}

    try:
        # Attempt to read existing data from the file
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        pass

    # Ensure that the "friends" key exists and is a list
    if "friends" not in data:
        data["friends"] = []

    # Check if the new friend's name is not already in the list
    if new_friend_name not in data["friends"]:
        # Add the new friend's name to the list
        data["friends"].append(new_friend_name)

        # Write the updated data back to the file
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
    else:
        print(f"{new_friend_name} already exists in the friend list.")

# Add a new friend to the list (only if they don't already exist)
new_friend_name = "Shubham"
add_friend(new_friend_name)
