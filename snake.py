from pytimedinput import timedInput
import os
import random
from colorama import Fore, init

def print_field():
    for cell in CELLS:
        if cell in snake_body:
            print(Fore.GREEN + 'X', end='')
        elif cell[0] in (0, FIELD_WIDTH - 1) or cell[1] in (0, FIELD_HEIGHT - 1):
            print(Fore.CYAN + '#', end='')
        elif cell == apple_pos:
            print(Fore.RED + '@', end='')
        else:
            print(' ', end='')

        if cell[0] == FIELD_WIDTH - 1:
            print('')


def update_snake():
    global eaten
    #head = snake_body[0]
    #new_head = (head[0] + direction[0], head[1] + direction[1])
    new_head = snake_body[0][0] + direction[0], snake_body[0][1] + direction[1]
    snake_body.insert(0, new_head)
    if not eaten:
        snake_body.pop(-1)
    eaten = False


def apple_collision():
    global apple_pos, eaten
    if apple_pos == snake_body[0]:
        apple_pos = place_apple()
        eaten = True


def place_apple():
    new_position = (random.randint(1, FIELD_WIDTH - 2), random.randint(1, FIELD_HEIGHT - 2))
    while new_position in snake_body:
        new_position = (random.randint(1, FIELD_WIDTH - 2), random.randint(1, FIELD_HEIGHT - 2))
    return new_position


init(autoreset= True)


# Settings
FIELD_WIDTH = 32
FIELD_HEIGHT = 16
CELLS = [(col,row) for row in range(FIELD_HEIGHT) for col in range(FIELD_WIDTH)]

# Snake
snake_body = [(5, FIELD_HEIGHT // 2), (4, FIELD_HEIGHT // 2), (3, FIELD_HEIGHT // 2)]
DIRECTIONS = {
        'left':  (-1,0),
        'rigth': (1,0),
        'up':    (0,-1),
        'down':  (0,1)
        }
# En la tupla de abajo el 1 representa el movimiento en horizontal(eje x) siendo por defecto 1 a la derecha
# y el cero representa el movimiento en vertical(eje y) siendo cero por defecto sin moverse
direction = DIRECTIONS['rigth']
eaten = False

# Apple
apple_pos = place_apple()


while True:
    # Clear the Field
    os.system('clear')

    # Field Drawing
    print_field()

    # Get input
    text,_ = timedInput('', timeout= 0.3)
    match text:
        case 'w': direction = DIRECTIONS['up']
        case 's': direction = DIRECTIONS['down']
        case 'a': direction = DIRECTIONS['left']
        case 'd': direction = DIRECTIONS['rigth']
        case 'q':
            # os.system('clear')
            break

    # Update the game
    update_snake()
    apple_collision()

    # Check death
    if snake_body[0][0] in (0, FIELD_WIDTH - 1) or \
       snake_body[0][1] in (0, FIELD_HEIGHT - 1) or \
       snake_body[0] in snake_body[1:]:
           break

