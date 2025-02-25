alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def caesar_shifr(string, user_shift):
    char_list = [(alphabet[(alphabet.index(sym) + user_shift) % len(alphabet)]
                  if sym in alphabet else sym)
                  for sym in string]
    new_str = ''.join(char_list)
    return new_str

input_str = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))
output_str = caesar_shifr(input_str, shift)
print('Зашифрованное сообщение: ', output_str)