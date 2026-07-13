"""
Name: Hamad Almansoori
Course: CS2430
Semester: Summer 2026

Programming Project 3
The Knapsack Problem

Purpose:
Implements the three greedy algorithms:
1. Highest Rating First
2. Lightest Weight First
3. Best Rating-to-Weight Ratio First
"""

MAX_WEIGHT = 700


# --------------------------------------------------
# Display selected experiments
# --------------------------------------------------
def print_solution(title, selected):

    total_weight = sum(item["weight"] for item in selected)
    total_rating = sum(item["rating"] for item in selected)

    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    print("{:<30} {:>10} {:>10}".format(
        "Experiment",
        "Weight",
        "Rating"))

    print("-" * 60)

    for item in selected:
        print("{:<30} {:>10} {:>10}".format(
            item["name"],
            item["weight"],
            item["rating"]))

    print("-" * 60)

    print(f"Total Weight : {total_weight} kg")
    print(f"Total Rating : {total_rating}")

    return total_weight, total_rating


# --------------------------------------------------
# Highest Rating First
# --------------------------------------------------
def highest_rating_first(experiments):

    ordered = sorted(
        experiments,
        key=lambda x: x["rating"],
        reverse=True
    )

    chosen = []
    weight = 0

    for item in ordered:

        if weight + item["weight"] <= MAX_WEIGHT:
            chosen.append(item)
            weight += item["weight"]

    return chosen


# --------------------------------------------------
# Lightest Weight First
# --------------------------------------------------
def lightest_first(experiments):

    ordered = sorted(
        experiments,
        key=lambda x: x["weight"]
    )

    chosen = []
    weight = 0

    for item in ordered:

        if weight + item["weight"] <= MAX_WEIGHT:
            chosen.append(item)
            weight += item["weight"]

    return chosen


# --------------------------------------------------
# Best Rating / Weight Ratio
# --------------------------------------------------
def ratio_first(experiments):

    ordered = sorted(
        experiments,
        key=lambda x: x["rating"] / x["weight"],
        reverse=True
    )

    chosen = []
    weight = 0

    for item in ordered:

        if weight + item["weight"] <= MAX_WEIGHT:
            chosen.append(item)
            weight += item["weight"]

    return chosen


# --------------------------------------------------
# Run all greedy strategies
# --------------------------------------------------
def run_greedy(experiments):

    results = {}

    selected = highest_rating_first(experiments)
    w, r = print_solution(
        "GREEDY STRATEGY 1 - HIGHEST RATING",
        selected)

    results["Highest Rating"] = (selected, w, r)

    selected = lightest_first(experiments)
    w, r = print_solution(
        "GREEDY STRATEGY 2 - LIGHTEST WEIGHT",
        selected)

    results["Lightest"] = (selected, w, r)

    selected = ratio_first(experiments)
    w, r = print_solution(
        "GREEDY STRATEGY 3 - BEST RATING / WEIGHT",
        selected)

    results["Ratio"] = (selected, w, r)

    return results
