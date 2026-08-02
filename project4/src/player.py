"""
Name: Hamad Almansoori
Course: CS2430

Programming Project 4 - Monopoly Simulation

Purpose:
Stores player information.
"""


class Player:


    def __init__(self):

        self.position = 0

        self.in_jail = False

        self.jail_attempts = 0

        self.get_out_card = 0



    def move(self, spaces):

        self.position = (self.position + spaces) % 40
