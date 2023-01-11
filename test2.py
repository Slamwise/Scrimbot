import json
import re

with open("results.json", "r") as f:
    data = json.load(f)

result_history = []
count = 1
for message in data:
    regex = r"\n[^\w]"

    cleaned = re.sub(regex, "*****", message["content"])

    print(cleaned.split("*****"))