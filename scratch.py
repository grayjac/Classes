#!/usr/bin/env python3


# ME499-S20 Python Lab 5
# Programmer: Jacob Gray
# Last Edit: 5/11/2020


import random


class GumballMachine:

    def __init__(self, capacity, cost):  # Calls stuff inside argument of class?

        # Object descriptors
        self.capacity = capacity
        self.cost = cost

        # State variables
        self.current_gumballs = capacity
        self.coins = 0

    def __str__(self):
        template = '<GumballMachine: {}/{}, costs {} coins per play>'
        return template.format(self.current_gumballs, self.capacity, self.cost)

    def __repr__(self):
        self.__str__()

    def spin_knob(self):

        if self.coins < self.cost:
            raise Exception("You haven't put enough coins in")

        self.coins -= self.cost
        if not self.current_gumballs:
            return None
        else:
            self.current_gumballs -= 1
            return random.choice(['Blue', 'Red', 'Green'])

    def insert_coin(self, num_coins):
        if num_coins < 0:
            raise ValueError("You can't take coins out of the machine")

        self.coins += num_coins

    def refill(self):
        self.current_gumballs = self.capacity


if __name__ == '__main__':
    machine = GumballMachine(5, 2)

    # object.attribute
    machine.insert_coin(10)  # Encapsulation - hiding inputs from the user so they don't fuck up your code - state issues

    print(machine.spin_knob())
    print(machine.spin_knob())
    print(machine.spin_knob())

    print(machine)
