#!/usr/bin/env python3


# ME499-S20 Python Lab 4 Problem 2
# Programmer: Jacob Gray
# Last Edit: 5/7/2020


from random import randint
import numpy as np
from random import randint


def simulate_gachapon(n):
    """
    Simulates a game with n total prizes. Each iteration should randomly generate an integer from 0 to n-1 and add
    it to the "prize pool".
    :param n: Number of prizes. Integer.
    :return: Number of iterations it takes to obtain all prizes.
    """

    prize_pool = []  # Empty list containing all prizes

    for elem in range(n):
        prize_pool.append(elem)

    my_prizes = []  # Empty list containing all my prizes through iteration
    counter = 0  # Will count how many iterations it takes to obtain every prize
    indexer = 0  # Variable to progress the while loop if the condition in it contains is met

    while indexer <= n:
        if prize_pool[indexer] not in my_prizes:
            my_prizes.append(randint(0, n - 1))
            counter += 1
        else:
            if indexer < n - 1:
                indexer += 1
            else:
                break

    return counter


def random_list(n):
    """
    Takes an integer n and returns a random list of length n, with integers uniformly sampled from 0 to n-1 (inclusive).
    :param n: Random integer.
    :return: A random list.
    """

    rand_list = []

    for i in range(n):
        rand_list.append(randint(0, n - 1))

    return rand_list


if __name__ == '__main__':
    print(simulate_gachapon(5))
