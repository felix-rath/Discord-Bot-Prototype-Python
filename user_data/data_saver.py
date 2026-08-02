import json
from pathlib import Path

START_MONEY = 1000
FILE_PATH = Path(__file__).parent / "data.json"

def set_money(user_id, value):
    create_file()

    user_id = str(user_id)

    with open(FILE_PATH, "r") as file:
        data = json.load(file)

    data[user_id] = {
        "money": value
    }

    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)


def load_money(user_id):
    create_file()
    with open (FILE_PATH, "r") as file:
        data = json.load(file)

    user_id = str(user_id)
    if user_id not in data:
        set_money(user_id, START_MONEY)
        return START_MONEY
    
    return data[user_id]["money"]


def create_file():
    file_path = Path(FILE_PATH)

    if not file_path.exists():
        with open(file_path, "w") as file:
            json.dump({}, file)
