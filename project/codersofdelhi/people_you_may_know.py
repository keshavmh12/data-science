import json
from collections import defaultdict

def load_data(filename):
    # This function is correct as written
    with open(filename, "r") as f:
        data = json.load(f)
    return data

def find_people_you_may_know(user_id, data):
    # 1. Map all user IDs to their set of friends for O(1) lookup
    user_friends = {}
    for user in data["users"]:
        user_friends[user["id"]] = set(user['friends'])

    # 2. Check if the user exists
    if user_id not in user_friends:
        return []

    direct_friends = user_friends[user_id]
    
    # 3. Use defaultdict to count mutual friends easily
    suggestions = defaultdict(int)
    
    # 4. Iterate through the user's direct friends (first degree)
    for friend_id in direct_friends:
        # Check if the friend_id is valid (e.g., in the data, though typically it should be)
        if friend_id in user_friends:
            # 5. Get the list of friends of the direct friend (second degree)
            friends_of_friend = user_friends[friend_id]
            
            for potential_friend_id in friends_of_friend:
                # 6. Skip the user themselves and people who are already direct friends
                if (potential_friend_id == user_id) or (potential_friend_id in direct_friends):
                    continue
                
                # 7. Count the mutual friends
                suggestions[potential_friend_id] += 1
    
    # 8. Sort suggestions by mutual friend count (descending)
    # The result is a list of (user_id, count) tuples
    sorted_suggestions = sorted(suggestions.items(), key=lambda x: x[1], reverse=True)
    
    # 9. Extract just the user IDs from the sorted list
    # The list comprehension correctly extracts the first element (user_id) from each tuple
    return [user_id_from_tuple for user_id_from_tuple, count in sorted_suggestions]

# load data (ensure 'data_cleaned.json' exists and is correctly formatted)
# Example data structure expected: {"users": [{"id": 1, "friends": [2, 3]}, {"id": 2, "friends": [1, 4]}, ...]}

data = load_data("data_cleaned.json")
user_id = int(input("Enter user ID to find people you may know: ")) 
recc = find_people_you_may_know(user_id, data)
print(recc)