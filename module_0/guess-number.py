#!/usr/bin/env python3

import numpy


def binary_search(number, start, end):
    """
    Searches a number in continuous array.

    Arguments:
        number (int) - number to be found in the array
        start  (int) - first number of the array
        end    (int) - latest number of the array

    Returns:
        amount of attempts were used
    """
    assert (start < end)
    assert (start <= number) and (number <= end)

    attempts = 0

    while True:
        guess = int((start + end) / 2)
        attempts = attempts + 1

        if guess < number:
            start = guess + 1
        elif guess > number:
            end = guess - 1
        elif guess == number:
            break

    return attempts


def guess_game(predictor, start=1, end=100, rounds=10**3):
    """
    Number prediction game.

    Arguments:
        predictor (func) - prediction algorithm
        start     (int)  - first  number of the range to predict from
        end       (int)  - latest number of the range to predict from
        rounds    (int)  - amount of game rounds

    Returns:
        mean of attempts to predict the number
    """
    guesses = list()
    randoms = numpy.random.randint(start, end + 1, size=rounds)

    for number in randoms:
        guesses.append(predictor(number, start, end))

    attempts = round(numpy.mean(guesses), 0)

    return attempts


if __name__ == "__main__":
    quality = \
        int(guess_game(binary_search))

    print("Guess rate is {} attempts".format(quality))
