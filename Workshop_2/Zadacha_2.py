hour = 0
tasks_sum =0
go_to_store = False

print('Начался 8-часовой рабочий день')

while hour != 8:
    hour +=1
    print(hour, 'час')
    solved_tasks = int(input('Сколько задач решит Максим? '))
    tasks_sum += solved_tasks
    call = int(input('Звонит жена. Взять трубку? '))
    if call == 1:
        go_to_store = True

print('Рабочий день закончился. Всего выполнено задач: ', tasks_sum)
if go_to_store:
    print('нужно зайти в магазин')