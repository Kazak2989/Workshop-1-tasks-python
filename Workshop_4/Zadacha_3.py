synonyms_dict = dict()
pairs_count = int(input('Введите количество пар слов: '))
for i_pairs in range(pairs_count):
    first_word, second_word = input(f'{i_pairs + 1} пара: ').lower().split('-')
    synonyms_dict[first_word] = second_word
    synonyms_dict[second_word] = first_word
while True:
    word = input('Введите слово: ').lower()
    if word in synonyms_dict:
        print('Синоним: ',synonyms_dict[word].capitalize())
        break
    else:
        print('Такого слова в словаре нет.')