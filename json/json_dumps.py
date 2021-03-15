import json

python_dict = {"name": "sorn & jim", "age": 21, "city": "chonburi"}

json_string = json.dumps(python_dict)

print(json_string)