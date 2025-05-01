import json, os


def add_email(email, filepath="subscribers.json"):
    data = {"emails": []}
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            data = json.load(f)
    if email not in data["emails"]:
        data["emails"].append(email)
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"{email} added.")
    else:
        print("Email already subscribed.")


def remove_email(email, filepath="subscribers.json"):
    with open(filepath, 'r') as f:
        data = json.load(f)
    if email in data["emails"]:
        data["emails"].remove(email)
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"{email} removed.")
    else:
        print("Email not found.")
