"""
Name: Hamad Almansoori
Course: CS2430
Semester: Summer 2026

Programming Project 3
The Knapsack Problem

Purpose:
Implements Dynamic Programming solution for the
0/1 Knapsack problem.

This file is optional extra credit.
"""


MAX_WEIGHT = 700



# --------------------------------------------------
# Dynamic Programming Knapsack Algorithm
#
# Idea:
#
# Create a table where:
#
# Rows = experiments considered
# Columns = possible weight limits
#
# Each cell stores the maximum rating possible
# for that combination.
#
# The decision at each step:
#
# 1. Do not include the experiment
# 2. Include the experiment if weight allows
#
# Choose the option with higher rating.
# --------------------------------------------------


def dynamic_programming(experiments):


    n = len(experiments)


    # Create DP table
    # Rows = number of experiments
    # Columns = weight capacity

    dp = []

    for i in range(n + 1):

        row = [0] * (MAX_WEIGHT + 1)

        dp.append(row)



    # Fill DP table

    for i in range(1, n + 1):

        weight = experiments[i-1]["weight"]

        rating = experiments[i-1]["rating"]


        for capacity in range(MAX_WEIGHT + 1):


            # Option 1:
            # Do not select experiment

            without_item = dp[i-1][capacity]


            # Option 2:
            # Select experiment

            if weight <= capacity:

                with_item = (
                    dp[i-1][capacity-weight]
                    + rating
                )

                dp[i][capacity] = max(
                    without_item,
                    with_item
                )

            else:

                dp[i][capacity] = without_item



    # ------------------------------------------
    # Backtracking to find selected experiments
    # ------------------------------------------

    selected = []

    capacity = MAX_WEIGHT


    for i in range(n, 0, -1):


        # If value changed,
        # the item was selected

        if dp[i][capacity] != dp[i-1][capacity]:


            selected.append(
                experiments[i-1]
            )


            capacity -= experiments[i-1]["weight"]



    selected.reverse()


    return selected, dp[n][MAX_WEIGHT]



# --------------------------------------------------
# Display DP Solution
# --------------------------------------------------

def print_dp_solution(selected, rating):


    print("\n")

    print("=" * 60)

    print("DYNAMIC PROGRAMMING SOLUTION")

    print("=" * 60)



    total_weight = 0



    for item in selected:

        print(
            f"{item['name']:<30}"
            f" Weight: {item['weight']} kg "
            f" Rating: {item['rating']}"
        )


        total_weight += item["weight"]



    print("-" * 60)


    print(
        f"Total Weight: {total_weight} kg"
    )


    print(
        f"Total Rating: {rating}"
    )
