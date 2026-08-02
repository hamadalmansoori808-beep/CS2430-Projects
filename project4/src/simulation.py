"""
Name: Hamad Almansoori
Course: CS2430

Programming Project 4 - Capstone: Monopoly Simulation

Purpose:
Runs Monopoly turns, movement rules,
jail strategies, and simulations.
"""


import random

from board import Board
from player import Player
from cards import Deck, chance_cards, community_cards



# Roll two dice

def roll_dice():

    die1 = random.randint(1,6)
    die2 = random.randint(1,6)

    return die1, die2



# Resolve Chance and Community Chest cards

def resolve_card(player, card):


    if card == "GO":

        player.position = 0


    elif card == "ILLINOIS":

        player.position = 24


    elif card == "ST_CHARLES":

        player.position = 11


    elif card == "BACK3":

        player.position = (player.position - 3) % 40


    elif card == "JAIL":

        player.position = 10

        player.in_jail = True



# Handle landing effects

def resolve_square(player, board, chance, community):


    name, square_type = board.get_square(player.position)


    if square_type == "CHANCE":

        card = chance.draw()

        resolve_card(player, card)



    elif square_type == "COMMUNITY":

        card = community.draw()

        resolve_card(player, card)



    elif square_type == "GO_TO_JAIL":

        player.position = 10

        player.in_jail = True



# Strategy A
# Leave immediately

def handle_jail_strategy_A(player):


    if player.in_jail:

        if player.get_out_card > 0:

            player.get_out_card -= 1

            player.in_jail = False


        else:

            player.in_jail = False



# Strategy B
# Try doubles for three turns

def handle_jail_strategy_B(player):


    if player.in_jail:

        while player.jail_attempts < 3:


            d1, d2 = roll_dice()


            if d1 == d2:

                player.in_jail = False

                player.jail_attempts = 0

                player.move(d1+d2)

                return


            else:

                player.jail_attempts += 1



        # failed after 3 tries

        player.in_jail = False

        player.jail_attempts = 0




# Simulate one complete turn

def simulate_turn(player, board, strategy):


    doubles = 0


    if player.in_jail:


        if strategy == "A":

            handle_jail_strategy_A(player)

        else:

            handle_jail_strategy_B(player)



    while True:


        d1, d2 = roll_dice()


        if d1 == d2:

            doubles += 1

        else:

            doubles = 0



        # three doubles sends to jail

        if doubles == 3:


            player.position = 10

            player.in_jail = True

            board.record_landing(10)

            return



        player.move(d1+d2)


        chance = Deck(chance_cards)

        community = Deck(community_cards)


        resolve_square(
            player,
            board,
            chance,
            community
        )


        board.record_landing(player.position)



        # stop if not doubles

        if d1 != d2:

            break




# Run many turns

def run_simulation(turns, strategy):


    board = Board()

    player = Player()


    for i in range(turns):

        simulate_turn(
            player,
            board,
            strategy
        )


    return board.landing_count
