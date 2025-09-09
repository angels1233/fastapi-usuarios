import json

with open("mock-users.json", "r", encoding="utf-8") as file:
    USERS = json.load(file)


def find_all():
    return USERS


def find_by_id(user_id: int):
    return next((user for user in USERS if user["id"] == user_id), None)
