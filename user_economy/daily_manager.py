from user_data import json_storage
from user_economy import economy_manager
from datetime import datetime, timedelta

DAILY_REWARD = 2000
DAILY_COOLDOWN = timedelta(hours=24)

LAST_DAILY_KEY = "last_daily"


async def can_claim_daily(user_id):
    last_daily = await json_storage.get_data(user_id, LAST_DAILY_KEY)

    if last_daily is None:
        return True

    last_daily = datetime.fromisoformat(last_daily)

    return datetime.now() - last_daily >= DAILY_COOLDOWN


async def claim_daily(user_id):
    if not await can_claim_daily(user_id):
        return None

    balance = await economy_manager.add_balance(
        user_id,
        DAILY_REWARD
    )

    await json_storage.set_data(
        user_id,
        LAST_DAILY_KEY,
        datetime.now().isoformat()
    )

    return balance