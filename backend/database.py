from model import Todo
# mongodb driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
db = client.todolist
collection = db.items

async def fetch_one_item(title):
    item = await collection.find_one({"title": title})
    return item

async def fetch_all_items():
    items = []
    cur = collection.find({})
    async for item in cur:
        items += [Todo(**item)]
    return items

async def create_item(data):
    item = data
    result = await collection.insert_one(item)
    return result

async def check_item(title):
    """find item and toggle check or unchecked"""
    item = fetch_one_item(title)
    state = item["done"]
    checked_item = await collection.update_one({"title": title}, {"$set": {"done": not state}})
    return checked_item

async def delete_item(title):
    await collection.delete_one({"title": title})
    return True