import json
import asyncio
from pathlib import Path

FILE_PATH = Path(__file__).parent / "users.json"

lock = asyncio.Lock()


def _create_file():
    if not FILE_PATH.exists():
        with open(FILE_PATH, "w") as file:
            json.dump({}, file)


async def set_data(user_id, key, value):
    _create_file()
    user_id = str(user_id)

    async with lock:
        with open(FILE_PATH, "r") as file:
            data = json.load(file)

        if user_id not in data:
            data[user_id] = {}

        data[user_id][key] = value

        with open(FILE_PATH, "w") as file:
            json.dump(data, file, indent=4)


async def get_data(user_id, key):
    _create_file()
    user_id = str(user_id)

    async with lock:
        with open(FILE_PATH, "r") as file:
            data = json.load(file)

        if user_id not in data:
            return None

        return data[user_id].get(key)