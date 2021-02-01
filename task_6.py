import re

hours = {}
with open("text_6.txt", "r") as file:
    for line in file.readlines():
        hours[re.findall(r'^\w+', line)[0]] = sum(map(int, re.findall(r'\d+', line)))
    print(hours)
