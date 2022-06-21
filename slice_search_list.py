import json


dict_list = {
    "mylist":  [
        {"myitem 1": "myitem value 1"},
        {"myitem 2": "myitem value 2"},
        {"myitem 3": "myitem value 3"},
        {"myitem 4": "myitem value 4"},
        {"myitem 5": "myitem value 5"},
        {"myitem 6": "myitem value 6"},
        {"myitem 7": "myitem value 7"},
        {"myitem 8": "myitem value 8"},
        {"myitem 9": "myitem value 9"},
        {"myitem 10": "myitem value 10"},
        {"myitem 11": "myitem value 11"},
        {"myitem 12": "myitem value 12"},
        {"myitem 13": "myitem value 13"},
        {"myitem 14": "myitem value 14"},
        {"myitem 15": "myitem value 15"},
        {"myitem 16": "myitem value 16"},
        {"myitem 17": "myitem value 17"},
        {"myitem 18": "myitem value 18"},
        {"myitem 19": "myitem value 19"},
        {"myitem 20": "myitem value 20"},
        {"myitem 21": "myitem value 21"},
        {"myitem 22": "myitem value 22"},
        {"myitem 23": "myitem value 23"},
        {"myitem 24": "myitem value 24"},
        {"myitem 25": "myitem value 25"},
        {"myitem 26": "myitem value 26"},
        {"myitem 27": "myitem value 27"},
        {"myitem 28": "myitem value 28"},
        {"myitem 29": "myitem value 29"},
        {"myitem 30": "myitem value 30"},
        {"myitem 31": "myitem value 31"},
        {"myitem 32": "myitem value 32"},
        {"myitem 33": "myitem value 33"},
        {"myitem 34": "myitem value 34"},
        {"myitem 35": "myitem value 35"},
        {"myitem 36": "myitem value 36"},
        {"myitem 37": "myitem value 37"},
        {"myitem 38": "myitem value 38"},
        {"myitem 39": "myitem value 39"},
        {"myitem 40": "myitem value 40"},
        {"myitem 41": "myitem value 41"},   
    ]
}

json_list = json.dumps(dict_list, indent=4)

items_per_page = 10
length = len(dict_list["mylist"])
pages = length / items_per_page
print(pages)

print(dict_list["mylist"][0:9])


# json_list["mylist"]
