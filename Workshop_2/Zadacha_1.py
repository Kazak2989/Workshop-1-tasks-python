rating = int(input('Введите число: '))
positive_count = 0
negative_count = 0

while rating !=0:
    if rating > 0:
        positive_count += 1
    else:
        negative_count +=1
    rating = int(input('Введите число: '))

print('Кол-во положительных чисел: ', positive_count)
print('Кол-во отрицательных чисел: ', negative_count)