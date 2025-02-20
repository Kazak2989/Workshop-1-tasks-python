video_card_numbera = int(input('Введите кол-во видеокарт: '))

video_cards = []
new_video_cards_list = []
max_item = 0

for item in range(video_card_numbera):
    video_cards.append(int(input(f'Видеокарта {item + 1}: ')))
    if video_cards[item] > max_item:
        max_item = video_cards[item]
for item in range(video_card_numbera):
    if video_cards[item] != max_item:
        new_video_cards_list.append(video_cards[item])
print()

print('Старый список видеокарт: [', end=' ')

for item in range(video_card_numbera):
    print(video_cards[item], end=' ')

print(']')

print('Новый список видеокарт: [', end= ' ')
for item in range(len(new_video_cards_list)):
    print(new_video_cards_list[item], end=' ')
print(']')
    