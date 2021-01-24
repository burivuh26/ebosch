def my_func(f1, f2, f3):
    my_list = [f1, f2, f3]
    try:
        my_list.remove(min(my_list))
        return sum(my_list)
    except TypeError:
        print('вводите числа')


print(my_func(2, 5, 58))
