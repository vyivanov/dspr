#!/usr/bin/env python3

import numpy


def predict(number, start, end):
    assert (start < end)
    assert (start <= number) and (number <= end)

    counter = 0

    while True:
        counter = counter + 1
        guess = int((start + end) / 2)
        if guess < number:
            start = guess + 1
        elif guess > number:
            end = guess - 1
        else:
            break

    return counter


def guess_game(predictor, start=1, end=100):
    guesses = list()
    randoms = numpy.random.randint(start, end + 1, size=10**5)

    for number in randoms:
        guesses.append(predictor(number, start, end))

    attempts = round(numpy.mean(guesses), 0)

    return attempts


if __name__ == "__main__":
    quality = int(guess_game(predict))
    print("Guess rate is {} attempts".format(quality))
