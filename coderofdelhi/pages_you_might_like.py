import json
import os

def load_data(filename):
    with open(filename,"r")as f:
        data=json.load(f)
    return data
    
def pages_you_might_like(user_id,data):
    user_pages = {}
    for user in data.get("users", []):
        user_pages[user['id']] = set(user.get("liked_pages", []))

    # if user not in data
    if user_id not in user_pages:
        return []

    liked_pages = user_pages[user_id]
    pages_suggestions = {}

    for other_user, pages in user_pages.items():
        if other_user == user_id:
            continue
        # pages is a set already; compute shared pages
        shared_pages = liked_pages.intersection(pages)
        if not shared_pages:
            continue

        # suggest pages the other user likes which current user doesn't
        for page in pages - liked_pages:
            pages_suggestions[page] = pages_suggestions.get(page, 0) + len(shared_pages)

    # sort suggestions by score (desc) then by page id (asc) for stable output
    sorted_pages = sorted(pages_suggestions.items(), key=lambda kv: (-kv[1], kv[0]))
    return [page_id for page_id, score in sorted_pages]

if __name__ == "__main__":
    # try the likely filenames in the repo (file has an odd name: massivedata,json)
    candidates = ["massivedata.json", "massivedata,json"]
    data_file = None
    for cand in candidates:
        if os.path.exists(cand):
            data_file = cand
            break

    if data_file is None:
        raise SystemExit("Could not find data file: try massivedata.json or massivedata,json in the project root")

    data = load_data(data_file)
    user_id = 2
    page_recc = pages_you_might_like(user_id, data)
    print("Suggested pages for user", user_id, "=>", page_recc)