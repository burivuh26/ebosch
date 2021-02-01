import json

with open('text_7.txt', 'r') as file:
    with open('text_77.json', 'w') as file_w:
        my_dict = {string.split()[0]: int(string.split()[2]) - int(string.split()[3]) for string in file}
        profit = []
        for i in my_dict.values():
            if i > 0:
                profit.append(i)
        json.dump([my_dict, {'profit': sum(profit) / len(profit)}], file_w, ensure_ascii=False, indent=4)
