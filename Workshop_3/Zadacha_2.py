films = ['Крепкий орешек','Назад в будущее','Таксист','Леон','Богемская рапсодия',
         'Город грехов','Мементо','Отступники','Деревня']

my_list = []
movies_count = int(input('Сколько фильмов хотите добавить?' ))
for _ in range(movies_count):
    movie = input('Введите название фильма: ')
    if movie in films:
        my_list.append(movie)
    else:
        print(f'Ошибка: фильма {movie} у нас нет: (')
print(f'\nВаш список любимых фильмов: {my_list}')