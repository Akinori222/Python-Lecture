import json

with open("example.json") as f:
    data = json.load(f)

# print(data)
print(data["glossary"]["GlossDiv"])

new_json = {"key1": "value1", "key2": (1, "value2")}
with open("new_json.json", mode="w") as f:
    json.dump(new_json, f)

