"""
Name: Hamad Almansoori
Course: CS2430

Programming Project 4 - Capstone: Monopoly Simulation

Purpose:
Analyzes simulation results and creates summary reports.
"""


import csv
import os



DATA_FOLDER = "../data"



# Monopoly square names for readable output

square_names = [

    "GO",
    "Mediterranean Avenue",
    "Community Chest",
    "Baltic Avenue",
    "Income Tax",
    "Reading Railroad",
    "Oriental Avenue",
    "Chance",
    "Vermont Avenue",
    "Connecticut Avenue",
    "Jail",
    "St. Charles Place",
    "Electric Company",
    "States Avenue",
    "Virginia Avenue",
    "Pennsylvania Railroad",
    "St. James Place",
    "Community Chest",
    "Tennessee Avenue",
    "New York Avenue",
    "Free Parking",
    "Kentucky Avenue",
    "Chance",
    "Indiana Avenue",
    "Illinois Avenue",
    "B&O Railroad",
    "Atlantic Avenue",
    "Ventnor Avenue",
    "Water Works",
    "Marvin Gardens",
    "Go To Jail",
    "Pacific Avenue",
    "North Carolina Avenue",
    "Community Chest",
    "Pennsylvania Avenue",
    "Short Line",
    "Chance",
    "Park Place",
    "Luxury Tax",
    "Boardwalk"

]



# Read CSV result

def read_csv(filename):


    path = os.path.join(
        DATA_FOLDER,
        filename
    )


    counts = []


    with open(path, "r") as file:


        reader = csv.reader(file)


        next(reader)


        for row in reader:

            counts.append(
                int(row[1])
            )


    return counts




# Find top squares

def top_squares(counts, number=5):


    result = []


    for index, value in enumerate(counts):

        result.append(
            (
                square_names[index],
                value
            )
        )


    result.sort(
        key=lambda x: x[1],
        reverse=True
    )


    return result[:number]




# Print summary

def analyze_file(filename):


    counts = read_csv(filename)


    print("\nFile:", filename)


    print("---------------------------")


    for name, count in top_squares(counts):

        print(
            name,
            ":",
            count
        )




# Compare two strategies

def compare_strategies():


    file_A = (

        "strategy_A_1000000_run_1.csv"

    )


    file_B = (

        "strategy_B_1000000_run_1.csv"

    )


    A = read_csv(file_A)

    B = read_csv(file_B)



    print("\n==========================")

    print("STRATEGY COMPARISON")

    print("==========================")



    differences = []



    for i in range(40):


        difference = abs(
            A[i] - B[i]
        )


        differences.append(
            (
                square_names[i],
                difference
            )
        )



    differences.sort(
        key=lambda x:x[1],
        reverse=True
    )


    print("\nLargest Differences:")


    for item in differences[:5]:

        print(
            item[0],
            ":",
            item[1]
        )




def main():


    print(
        "MONOPOLY SIMULATION ANALYSIS"
    )


    print(
        "============================"
    )



    analyze_file(

        "strategy_A_1000000_run_1.csv"

    )


    analyze_file(

        "strategy_B_1000000_run_1.csv"

    )



    compare_strategies()




if __name__ == "__main__":

    main()
