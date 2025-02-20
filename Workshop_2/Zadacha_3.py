number = 7
guess_count = 0

while True:
    guess_num = int(input('Введите число: '))
    guess_count += 1
    if guess_num > number:
        print('Число больше, чем нужно. Попробуйте еще раз!')
    elif guess_num < number:
        print('Число меньше, чем нужно. Попробуйте еще раз!')
    else:
        print('Выв угадали! Число попыток: ',guess_count)
        break