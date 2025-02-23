array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

all_elements = array_1 + array_2 + array_3

new_elements_1 = []

for elements in all_elements:
    if elements not in new_elements_1 and all(elements in array for array in [array_1, array_2,array_3]):
        new_elements_1.append(elements)
print('Решение без множеств: ', new_elements_1)

new_elements_1_set = set(array_1) & set(array_2) & set(array_3)

print('Решение с использованием множеств: ', new_elements_1_set)

# Задача 2: найти элементы из первого списка, которых нет во втором и третьем списках\

new_elements_2 = []
for elements in array_1:
    if elements not in array_2 and elements not in array_3:
        new_elements_2.append(elements)
print('Решение без множеств: ', new_elements_2)

new_elements_2_set = set(array_1) - set(array_2) - set(array_3)

print('Решение с множествами: ', new_elements_2_set)
