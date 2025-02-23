def is_poly(string):
    char_dict = dict()
    for i_sum in string:
        char_dict[i_sum] = char_dict.get(i_sum, 0) + 1
    odd_count = 0
    for i_value in char_dict.values():
        if i_value % 2 != 0:
            odd_count += 1
    return odd_count <=1
my_string = input('Введите строку: ')
if is_poly(my_string):
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')