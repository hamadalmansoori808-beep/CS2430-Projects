"""
Name: Hamad Almansoori
Course: CS2430
Semester: Summer 2026

Programming Project 3
The Knapsack Problem

Purpose:
Main program that runs greedy algorithms,
brute-force search, and dynamic programming.
"""


from greedy import run_greedy
from brute_force import run_brute_force
from dp import dynamic_programming, print_dp_solution



# Maximum payload weight

MAX_WEIGHT = 700



# --------------------------------------------------
# Experiment Data
# Format:
# Name, Weight, Rating
# --------------------------------------------------

experiments = [

    {
        "name": "Cloud Patterns",
        "weight": 36,
        "rating": 5
    },

    {
        "name": "Solar Flares",
        "weight": 264,
        "rating": 9
    },

    {
        "name": "Solar Power",
        "weight": 188,
        "rating": 6
    },

    {
        "name": "Binary Stars",
        "weight": 203,
        "rating": 8
    },

    {
        "name": "Relativity",
        "weight": 104,
        "rating": 8
    },

    {
        "name": "Seed Viability",
        "weight": 7,
        "rating": 4
    },

    {
        "name": "Sun Spots",
        "weight": 90,
        "rating": 2
    },

    {
        "name": "Mice Tumors",
        "weight": 65,
        "rating": 8
    },

    {
        "name": "Microgravity Plant Growth",
        "weight": 75,
        "rating": 5
    },

    {
        "name": "Micrometeorites",
        "weight": 170,
        "rating": 9
    },

    {
        "name": "Cosmic Rays",
        "weight": 80,
        "rating": 7
    },

    {
        "name": "Yeast Fermentation",
        "weight": 27,
        "rating": 4
    }

]



# --------------------------------------------------
# Comparison Summary
# --------------------------------------------------

def comparison_summary(greedy_results, brute_results, dp_result):


    print("\n")

    print("=" * 70)

    print("FINAL COMPARISON SUMMARY")

    print("=" * 70)



    print(
        "{:<30} {:>15} {:>15}".format(
            "Strategy",
            "Weight",
            "Rating"
        )
    )


    print("-" * 70)



    for name, result in greedy_results.items():

        print(
            "{:<30} {:>15} {:>15}".format(
                name,
                result[1],
                result[2]
            )
        )



    optimal = brute_results[0]


    print(
        "{:<30} {:>15} {:>15}".format(
            "Brute Force Optimal",
            optimal["weight"],
            optimal["rating"]
        )
    )


    print(
        "{:<30} {:>15} {:>15}".format(
            "Dynamic Programming",
            sum(
                item["weight"]
                for item in dp_result[0]
            ),
            dp_result[1]
        )
    )



    print("-" * 70)



    best_greedy = max(
        greedy_results.items(),
        key=lambda x:x[1][2]
    )


    print(
        f"Best Greedy Strategy: {best_greedy[0]}"
    )


    print(
        f"Optimal Rating: {optimal['rating']}"
    )



# --------------------------------------------------
# Main Program
# --------------------------------------------------

def main():


    print("=" * 70)

    print("CS2430 PROGRAMMING PROJECT 3")

    print("THE KNAPSACK PROBLEM")

    print("=" * 70)



    print("\nTotal Experiments:", len(experiments))

    print("Maximum Weight:", MAX_WEIGHT, "kg")



    # Run greedy methods

    greedy_results = run_greedy(experiments)



    # Run brute force

    brute_results = run_brute_force(experiments)



    # Run DP

    selected, rating = dynamic_programming(experiments)


    print_dp_solution(
        selected,
        rating
    )


    # Comparison

    comparison_summary(
        greedy_results,
        brute_results,
        (selected, rating)
    )



    print("\nProgram Completed Successfully")



if __name__ == "__main__":

    main()
