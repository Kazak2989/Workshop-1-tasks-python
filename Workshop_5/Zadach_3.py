def my_sum(*args):
    total_sum = 0
    for i_element in args:
        if isinstance(i_element, int):
            total_sum += i_element
        elif isinstance(i_element,(list, tuple)):
            for x in i_element:
                total_sum += my_sum(x)
    return total_sum

print(my_sum([[1, 2, [3]], [1], 3])) 
print(my_sum(1, 2, 3, 4, 5))