import json
from random import randint
from datetime import datetime
str_json = """
{
    "response": {
        "count": 5475869271,
        "items": [{
            "first_name": "name1",
            "id": 65859300101,
            "last_name": "name2",
            "can_access_closed": false,
            "is_closed": true,
            "photo": "kgugu"
        }, {
            "first_name": "name1",
            "id": 6585913243564,
            "last_name": "name2",
            "can_access_closed": false,
            "is_closed": true,
            "photo": "kgugu"
        }]
    }
}
"""
data = json.loads(str_json)
for item in data["response"]["items"]:
    del item['id']
    item['likes'] = randint(100, 200)
    item['nul'] = None
    item['time'] = datetime.now().strftime('%d/%m/%y')
    print(data["response"]["items"])

# new_json = json.dumps(data, indent=4)
# print(new_json)
with open('my.json', 'w') as file:
    json.dump(data, file, indent=4)

with open('my.json') as file:
    data = json.load(file)
    print(data)
