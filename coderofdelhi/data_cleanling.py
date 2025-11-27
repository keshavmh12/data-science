import json
def clean_data(data):
    #reomve user with missing name
    data["users"]=[user for user in data["users"] if user["name"].strip()]

    #remove page with duplicate freinds
    for users in data["users"]:
        users["friends"]=list(set(users["friends"]))

    #remove inactive users
    data["users"]=[user for user in data["users"] if user["friends"] or user["liked_pages"]]
    
    #remove uplicate pages
    uniqe_pages={}
    for page in data["pages"]:
        uniqe_pages[page['id']] = page
    data["pages"]=list(uniqe_pages.values())    
        
    return data

#load data from json file
data=json.load(open("data1.json","r"))
data=clean_data(data)
json.dump(data,open("data_cleaned.json","w"),indent=4)
print("successfully cleaned data and saved to data_cleaned.json")