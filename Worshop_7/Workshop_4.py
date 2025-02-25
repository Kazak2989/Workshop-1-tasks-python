def count_unique_characters(string):
    lower_string = string.lower()
    unique_chars = list(filter(lambda c: lower_string.count(c.lower()) == 1, lower_string))
    print(unique_chars)
    return len(unique_chars)

message = "Today is a beautiful day! The sun is shining and the birds are singing."

unique_count = count_unique_characters(message)
print('Кол-во уникальных символов в строке: ', unique_count)