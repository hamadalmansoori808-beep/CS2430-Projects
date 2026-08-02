"""
Name: Hamad Almansoori
Course: CS2430

Programming Project 4 - Capstone: Monopoly Simulation

Purpose:
Defines the Monopoly board and tracks landing frequencies.
"""


class Board:

    def __init__(self):

        self.squares = [

            ("GO", "GO"),
            ("Mediterranean Avenue", "PROPERTY"),
            ("Community Chest", "COMMUNITY"),
            ("Baltic Avenue", "PROPERTY"),
            ("Income Tax", "TAX"),
            ("Reading Railroad", "RAILROAD"),
            ("Oriental Avenue", "PROPERTY"),
            ("Chance", "CHANCE"),
            ("Vermont Avenue", "PROPERTY"),
            ("Connecticut Avenue", "PROPERTY"),
            ("Jail", "JAIL"),
            ("St. Charles Place", "PROPERTY"),
            ("Electric Company", "UTILITY"),
            ("States Avenue", "PROPERTY"),
            ("Virginia Avenue", "PROPERTY"),
            ("Pennsylvania Railroad", "RAILROAD"),
            ("St. James Place", "PROPERTY"),
            ("Community Chest", "COMMUNITY"),
            ("Tennessee Avenue", "PROPERTY"),
            ("New York Avenue", "PROPERTY"),
            ("Free Parking", "FREE"),
            ("Kentucky Avenue", "PROPERTY"),
            ("Chance", "CHANCE"),
            ("Indiana Avenue", "PROPERTY"),
            ("Illinois Avenue", "PROPERTY"),
            ("B&O Railroad", "RAILROAD"),
            ("Atlantic Avenue", "PROPERTY"),
            ("Ventnor Avenue", "PROPERTY"),
            ("Water Works", "UTILITY"),
            ("Marvin Gardens", "PROPERTY"),
            ("Go To Jail", "GO_TO_JAIL"),
            ("Pacific Avenue", "PROPERTY"),
            ("North Carolina Avenue", "PROPERTY"),
            ("Community Chest", "COMMUNITY"),
            ("Pennsylvania Avenue", "PROPERTY"),
            ("Short Line", "RAILROAD"),
            ("Chance", "CHANCE"),
            ("Park Place", "PROPERTY"),
            ("Luxury Tax", "TAX"),
            ("Boardwalk", "PROPERTY")
        ]

        self.landing_count = [0] * 40


    def get_square(self, position):

        return self.squares[position]


    def record_landing(self, position):

        self.landing_count[position] += 1


    def reset(self):

        self.landing_count = [0] * 40
