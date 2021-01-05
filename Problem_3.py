
# Write a Python program to convert Python dictionary object (sort by key) to JSON data. Print the object members with indent level 4.

import json

dict_obj = {5: "laxmi", 4: "ganesh", 3: "krishna", 2: "mandire", 1: "thumura"}
print(json.dumps(dict_obj, sort_keys=True, indent=4))
