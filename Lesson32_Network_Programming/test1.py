from Task2_Caesar import Caesar_cipher

key = -5
text = Caesar_cipher(key, 'Слово')
print(text)
print('Перевірка повідомлення: ', Caesar_cipher(-key, text))