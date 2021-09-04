import random


def main(number):
    """
    game of hi - lo
    for Michael's Pycharm course
    4 September 2021
    """
    print("Welcome to the HI - LO game")
    turns = 6
    while turns > 0:
        response = int(input('Guess a number between 1 & 100: '))
        if response == number:
            return f"Got it! The number is {number}"
        if response > number:
            print('Too high!')
        else:
            print('Too low!')
        turns += 1
    return 'You lost'


if __name__ == '__main__':
    print(main(random.randint(1, 100)))
