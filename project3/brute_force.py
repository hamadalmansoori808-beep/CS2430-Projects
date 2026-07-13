"""
Name: Hamad Almansoori
Course: CS2430
Semester: Summer 2026

Programming Project 3
The Knapsack Problem

Purpose:
Implements brute-force exhaustive search.
Checks every possible subset of experiments
and finds the best valid payload combinations.
"""


MAX_WEIGHT = 700


# --------------------------------------------------
# Calculate total weight and rating
# --------------------------------------------------
def calculate_totals(subset):

    total_weight = 0
    total_rating = 0

    for item in subset:

        total_weight += item["weight"]
        total_rating += item["rating"]

    return total_weight, total_rating



# --------------------------------------------------
# Generate all possible subsets
# 2^12 = 4096 combinations
# --------------------------------------------------
def generate_subsets(experiments):

    subsets = []

    n = len(experiments)

    total_combinations = 2 ** n


    for mask in range(total_combinations):

        subset = []


        for i in range(n):

            # Check if experiment is included
            if mask & (1 << i):

                subset.append(experiments[i])


        subsets.append(subset)


    return subsets



# --------------------------------------------------
# Find valid solutions
# --------------------------------------------------
def find_valid_solutions(experiments):

    all_subsets = generate_subsets(experiments)

    valid_solutions = []


    for subset in all_subsets:

        weight, rating = calculate_totals(subset)


        # Only keep solutions under 700 kg
        if weight <= MAX_WEIGHT:

            valid_solutions.append(
                {
                    "items": subset,
                    "weight": weight,
                    "rating": rating
                }
            )


    return valid_solutions



# --------------------------------------------------
# Get top 3 solutions
# --------------------------------------------------
def get_top_three(experiments):

    solutions = find_valid_solutions(experiments)


    # Sort by highest rating
    # If ratings are equal, prefer lighter weight
    solutions.sort(
        key=lambda x: (
            x["rating"],
            -x["weight"]
        ),
        reverse=True
    )


    return solutions[:3]



# --------------------------------------------------
# Display brute force results
# --------------------------------------------------
def print_brute_force_results(top_three):


    print("\n")
    print("=" * 60)
    print("BRUTE FORCE RESULTS - TOP 3 SOLUTIONS")
    print("=" * 60)



    for index, solution in enumerate(top_three):

        print("\n")
        print(f"RANK {index + 1}")
        print("-" * 60)


        for item in solution["items"]:

            print(
                f"{item['name']:<30}"
                f" Weight: {item['weight']} kg "
                f" Rating: {item['rating']}"
            )


        print("-" * 60)

        print(
            f"Total Weight: {solution['weight']} kg"
        )

        print(
            f"Total Rating: {solution['rating']}"
        )


        if index == 0:

            print(">>> OPTIMAL SOLUTION <<<")



# --------------------------------------------------
# Run brute force search
# --------------------------------------------------
def run_brute_force(experiments):

    top_three = get_top_three(experiments)

    print_brute_force_results(top_three)

    return top_three
