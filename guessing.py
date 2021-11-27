number = 78
# Число для угадывания
# 1. Запрос имя пользователя
user = input('Введите ваше имя ')
# 2. Запрос цифры от 1 до 100
guess = int(input(f'Введите число от 1 до 100, {user} '))
# 3. Вывод «угадал» или «не угадал»
victory = guess == number
defeat = guess != number
print('угадал'*victory, end='' 'Не угадал'*defeat)
