from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbmakingchallenge

food = [
    {'name':'김치찌개', '맵기':'y', '국물':'y', '누적':0},
    {'name':'아구찜', '맵기':'y', '국물':'n', '누적':0},
    {'name': '설렁탕', '맵기': 'n', '국물': 'y', '누적': 0},
    {'name': '족발', '맵기': 'n', '국물': 'n', '누적': 0},

]
db.foods.insert_many(food)