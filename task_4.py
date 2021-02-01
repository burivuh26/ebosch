with open("text_4_new.txt", "w") as file_new:
    with open("text_4.txt", "r") as file:
        translate_dict = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}
        file_new.writelines([line.replace(line.split()[0], translate_dict.get(line.split()[0])) for line in file])

