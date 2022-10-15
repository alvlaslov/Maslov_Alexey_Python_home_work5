# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


# Option man vs man
# P.S. Для того, чтобы выиграть игру необходимо при каждом ходе придерживаться формулы
# (ОСТm+1N),где ОСТ - остаток от деления N на m+1, N - число конфет на столе, m - максимальное число конфет, к-ое возможно взять за ход.


from random import randint
box = 221
min_pos = 1
max_pos = 28

def take_candies(player):
    c = int(input(f'{player}, How many candies will you take (from 1 to 28)?'))
    while c > max_pos or c < min_pos:
        c = int(input(f'{player}, Input number from 1 to 28: '))
    return c

def smart_bot(remains):
    c = remains % (max_pos + 1)
    if c == 0:
        c = randint(min_pos, min_pos + 5)
    return c

def result(player, quantity, total, remains):
    print(f'{player} took {quantity} candies and has {total} candies. There are {remains} candies on the desk.')

print(f"The game 'Take all the candies!' welcomes you.\n"
      f"Condition: There is 2021 candies on the table.\n"
      f"The players make a move after each other.\n"
      f"In one move, you can pick up no more than 28 candies.\n"
      f"All the opponent's candies go to the one who made the last move.\n"
      f"The first move is determined by drawing lots.\n"
      f"Your opponent is the smart bot.\n"
      f"Let's go!!!")
fp_name = input('Player introduce yourself: ')
sp_name = 'Smart bot'
pos = randint(0, 1)
if pos > 0:
    print(f'Congratulations!!! {fp_name}, you go first.')
else:
    print(f'{sp_name} goes first.')
fp_counter = 0
sp_counter = 0
while box > max_pos:
    if pos:
        num = take_candies(fp_name)
        fp_counter += num
        box -= num
        pos = 0
        result(fp_name, num, fp_counter, box)
    else:
        num = smart_bot(box)
        sp_counter += num
        box -= num
        pos = 1
        result(sp_name, num, sp_counter, box)

if pos:
    print(f'The winner is {fp_name}!!!')
else:
    print(f'The winner is {sp_name}!!!')







