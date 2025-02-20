original_list = [1,4,-3,0,10]
print('Изначальный список: ', original_list)
for i in range(len(original_list) - 1):
    for j in range(len(original_list) - 1 - i):
        if original_list[j] > original_list[j + 1]:
            original_list[j], original_list[j + 1] = original_list[j+1], original_list[j]

print('Отсортированный список: ', original_list)