minutes = int(input('Введите количество минут: '))
hours = minutes // 60
rest_minutes = minutes% 60

print('Часов', hours)
print('Осталось минут: ', rest_minutes)