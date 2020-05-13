#!/usr/bin/env python3


# ME499-S20 Python Lab 5
# Programmer: Jacob Gray
# Last Edit: 5/12/2020


import sys
from utils import simulate_gachapon
import numpy as np


class GachaponSimulator:

    def __init__(self, prizes_n):
        # Object descriptors
        self.prizes_n = prizes_n

        # State variables
        self.results = []

    def _simulate_once(self):
        return simulate_gachapon(self.prizes_n)

    def reset(self):
        self.results.clear()
        return 'Results list successfully reset!'

    def simulate(self, num_games):
        for i in range(num_games):
            self.results.append(simulate_gachapon(self.prizes_n))

    def get_summary_stats(self):

        n = len(self.results)

        if n == 0:
            mean = None
            ststd = None

        elif n == 1:
            mean = np.mean(self.results)
            ststd = None

        else:
            mean = np.mean(self.results)
            ststd = np.std(self.results)

        return {'n': n, 'mean': mean, 'stdev': ststd}


if __name__ == '__main__':
    if len(sys.argv) <= 2:
        print('Please enter a valid prize pool size, "n", and number of games to play, "num_games"')
        print(r"Example: PycharmProjects\Classes\gachapon.py 10 1000")
        sys.exit(0)

    print('Running {}-prize lottery simulator {} times...'.format(sys.argv[1], sys.argv[2]))
    my_sim = GachaponSimulator(10)
    my_sim.simulate(2)
    my_dict = my_sim.get_summary_stats()
    print('Average number of iterations was {}, '
          'with a mean of {} '
          'and a standard deviation of {}'.format(my_dict['n'], my_dict['mean'], my_dict['stdev']))
