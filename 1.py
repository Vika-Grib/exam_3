'''Напишите функцию, которая будет принимать номер кредитной карты и
показывать только последние 4 цифры. Остальные цифры должны заменяться
звездочками'''


def card_number(card):
    return '*' * len(card[:-4]) + card[-4:]

number = input('Введите номер карты: ')
print(card_number(number))