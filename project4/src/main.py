"""
Name: Hamad Almansoori
Course: CS2430

Programming Project 4 - Capstone: Monopoly Simulation

Purpose:
Runs all Monopoly simulations and saves results.
"""


import csv
import os

from simulation import run_simulation



# Folder for saved results

DATA_FOLDER = "../data"



# Create data folder if missing

if not os.path.exists(DATA_FOLDER):

    os.makedirs(DATA_FOLDER)



# Required simulation sizes

turn_values = [

    1000,
    10000,
    100000,
    1000000

]



# Number of independent simulations

runs = 10




# Save results to CSV

def save_results(filename, counts, turns):


    path = os.path.join(DATA_FOLDER, filename)


    with open(path, "w", newline="") as file:


        writer = csv.writer(file)


        writer.writerow(
            [
                "Square Number",
                "Landing Count",
                "Percentage"
            ]
        )


        for index, count in enumerate(counts):


            percentage = (count / turns) * 100


            writer.writerow(
                [
                    index,
                    count,
                    round(percentage, 4)
                ]
            )



# Run simulations

def main():


    strategies = [

        "A",
        "B"

    ]


    for strategy in strategies:


        print("\n==============================")

        print(
            "Running Strategy",
            strategy
        )

        print("==============================")



        for turns in turn_values:


            for run in range(1, runs + 1):


                print(
                    "Strategy:",
                    strategy,
                    "| Turns:",
                    turns,
                    "| Run:",
                    run
                )


                results = run_simulation(
                    turns,
                    strategy
                )



                filename = (

                    f"strategy_{strategy}_"
                    f"{turns}_"
                    f"run_{run}.csv"

                )


                save_results(

                    filename,
                    results,
                    turns

                )



    print("\nSimulation Completed Successfully")




if __name__ == "__main__":

    main()
