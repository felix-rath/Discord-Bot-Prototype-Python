from user_data import json_storage

KEY = "money"
START_BALANCE = 10000

async def set_balance(user_id, value):
    await json_storage.set_data(user_id, KEY, value)


async def add_balance(user_id, value):
    balance = await json_storage.get_data(user_id, KEY)

    if balance is None:
        balance = START_BALANCE

    await set_balance(
        user_id,
        balance + value
    )
    return balance + value


async def remove_balance(user_id, value):
    balance = await json_storage.get_data(user_id, KEY)
    balance = balance - value

    if balance < 0:
        return None

    await set_balance(user_id, balance)
    return balance


async def get_balance(user_id):
    balance = await json_storage.get_data(user_id, KEY)
    if balance is None:
        await set_balance(user_id, START_BALANCE)
        balance = await json_storage.get_data(user_id, KEY)
    return balance