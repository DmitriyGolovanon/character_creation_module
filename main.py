# character_creation_module/main.py

from random import randint

# Новый импорт.
# Из модуля start_game_banner, который расположен в папке graphic_arts,
# импортируем функцию run_screensaver().
from graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str, char_class: str) -> str:
    value_attack: int = 0
    if char_class == 'warrior':
        value_attack = 5 + randint(3, 5)
    if char_class == 'mage':
        value_attack = 5 + randint(5, 10)
    if char_class == 'healer':
        value_attack = 5 + randint(-3, -1)
    return (f'{char_name} нанёс урон противнику равный {value_attack}')


def defence(char_name: str, char_class: str) -> str:
    value_defence: int = 0
    if char_class == 'warrior':
        value_defence = 10 + randint(5, 10)
    if char_class == 'mage':
        value_defence = 10 + randint(-2, 2)
    if char_class == 'healer':
        value_defence = 10 + randint(2, 5)
    return (f'{char_name} блокировал {value_defence} урона')


def special(char_name: str, char_class: str) -> str:
    val_special: int = 0
    if char_class == 'warrior':
        val_special = 80 + 25
    if char_class == 'mage':
        val_special = 5 + 40
    if char_class == 'healer':
        val_special = 10 + 30
    return (f'{char_name} применил специальное умение «Защита {val_special}»')


def start_training(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.'
          'Введи одну из команд: attack — чтобы атаковать противника,'
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.'
          'Если не хочешь тренироваться, введи команду skip.')
    cmd: str = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        print('Введи название персонажа, за которого хочешь играть: '
              'Воитель — warrior, Маг — mage, Лекарь — healer: ')
        char_class = input()
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. '
                  'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. '
                  'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. '
                  'Черпает силы из природы, веры и духов.')
        print('Нажми (Y), чтобы подтвердить выбор, или любую другую кнопку, '
              'чтобы выбрать другого персонажа ')
        approve_choice = input().lower()
    return char_class


def main():
    run_screensaver()
    print('Приветствую тебя, искатель приключений!'
          'Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:'
          'Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
