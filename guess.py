from random import randint
STOP_GAME = None
COUNTER = 0

def hello():
    print('''
Welcome to GUESS number.
The rules are quite simple, you have 5 attempts,
we will remind you when the last one remains,
I advise you to use binary search.
     ''')

hello()
stop = int(input('Enter the end of range >> '))
print(f'[!] The number is generated! You have selected a range from 1 to {stop}!\n')
GUESS = randint(1, stop)

def conditions(user_number):
    global STOP_GAME, COUNTER
    user_number = int(user_number)
    if user_number > GUESS:
        COUNTER += 1
        print(f'[HOT] Oh no, your number is bigger than ours. {GUESS}')
    elif user_number < GUESS:
        COUNTER += 1
        print(f'[COLDY] Oh no, your number is less than ours. {GUESS}')
    else:
        print(f'*** Congrats! You did it. ***')
        ask_continue()

def playing_game():
    global STOP_GAME
    while STOP_GAME != True:
        user_number = input(f'[?] {GUESS} Enter a number >> ')
        if is_valid(user_number):
            conditions(user_number)
        if COUNTER == 5:
            print('[-_-] Unfortunately you couldn\'t :)\n')
            ask_continue()
        elif COUNTER == 4:
            print()
            print('[1] You have one last attempt!\n')
            

def ask_continue():
    global STOP_GAME, GUESS, stop
    match input('[?] Don\'t you want to continue? (+/-) '):
        case '+':
            stop = int(input('Enter the end of range >> '))
            GUESS = randint(1, stop)
            print(f'[!] The number is generated! You have selected a range from 1 to {stop}!\n')

        case '-':
            print('[!] Thank your for playing!')
            STOP_GAME = True
        case _:
            print()
            print('[!] Upps, you didn\'t enter a number! (+ or -)\n')
            ask_continue()

def is_valid(value):
    try:
        number = int(value)
        assert 1 <= number <= stop, f'[!] A mistake. The number must be in the range from 1 to {stop}.'
        return number
    except ValueError:
        print('Don\'t you think you were driving a wrong number?')
    except AssertionError as Error:
        print(Error)

playing_game()