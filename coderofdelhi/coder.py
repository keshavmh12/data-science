import json
# function for read data from json file
def load_data(filename):
    with open(filename , "r") as f:
        data =json.load(f)
    return data


# finction for the user and their connections
def display_user(data):
    print("users information and their connections: ")
    for user in data["users"]:
        print(
            f"ID: {user['id']}, "
            f"is the friends with: {user['friends']}, "
            f"and liked pages are: {user['liked_pages']}" 
        )
    print("\npages information:")
    for page in data["pages"]:
            print(f"{page["id"]}:{page["name"]}")
display_user(load_data("data.json"))
