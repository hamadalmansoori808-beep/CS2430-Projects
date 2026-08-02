"""
Name: Hamad Almansoori
Course: CS2430

Programming Project 4 - Monopoly Simulation

Purpose:
Creates Chance and Community Chest decks.
"""


import random



class Deck:


    def __init__(self, cards):

        self.cards = cards.copy()

        self.discard = []

        random.shuffle(self.cards)



    def draw(self):

        if len(self.cards) == 0:

            self.cards = self.discard

            self.discard = []

            random.shuffle(self.cards)


        card = self.cards.pop()

        self.discard.append(card)

        return card



chance_cards = [

    "GO",

    "ILLINOIS",

    "ST_CHARLES",

    "JAIL",

    "BACK3",

    "NONE"

]



community_cards = [

    "GO",

    "JAIL",

    "NONE",

    "NONE"

]
