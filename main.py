"""Сharacter creation module."""

from random import randint

# Из модуля start_game_banner, который расположен в папке graphic_arts,
# импортируем функцию run_screensaver().
from graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str, char_class: str) -> str:
    """Return character's attack value, depending on his class."""
    if char_class == 'warrior':
        damage = randint(3, 5)
    elif char_class == 'mage':
        damage = randint(5, 10)
    elif char_class == 'healer':
        damage = randint(-3, -1)
    return (f'{char_name} нанёс урон противнику равный {5 + damage}')


def defence(char_name: str, char_class: str) -> str:
    """Return character's defence value, depending on his class."""
    if char_class == 'warrior':
        defended = randint(5, 10)
    elif char_class == 'mage':
        defended = randint(-2, 2)
    elif char_class == 'healer':
        defended = randint(2, 5)
    return (f'{char_name} блокировал {10 + defended} урона')


def special(char_name: str, char_class: str) -> str:
    """Return special action text, depending on character's class."""
    action = 'применил специальное умение'
    if char_class == 'warrior':
        ability = 'Выносливость'
        spec_value = 105
    elif char_class == 'mage':
        ability = 'Атака'
        spec_value = 45
    elif char_class == 'healer':
        ability = 'Защита'
        spec_value = 40
    else:
        return (f'{char_name} не {action}')
    return (f'{char_name} {action} «{ability} {spec_value}»')


def start_training(char_name: str, char_class: str) -> str:
    """Check the operation of the attack defense or special skill functions."""
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    elif char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    elif char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.\n',
          'Введи одну из команд: attack — чтобы атаковать противника, ',
          'defence — чтобы блокировать атаку противника ',
          'или special — чтобы использовать свою суперсилу.\n',
          'Если не хочешь тренироваться, введи команду skip.',
          sep='',
          )
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
    """Wait for input to return character's class string value."""
    approve_choice: str = ''
    char_class: str = ''
    message = 'Введи название персонажа, за которого хочешь играть: '
    choice = 'Воитель — warrior, Маг — mage, Лекарь — healer: '
    while approve_choice != 'y':
        char_class = input(message + choice)
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя.',
                  'Сильный, выносливый и отважный.',
                  )
        elif char_class == 'mage':
            print('Маг — находчивый воин дальнего боя.',
                  'Обладает высоким интеллектом.',
                  )
        elif char_class == 'healer':
            print('Лекарь — могущественный заклинатель.',
                  'Черпает силы из природы, веры и духов.',
                  )
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
