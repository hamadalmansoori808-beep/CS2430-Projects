"""
Name: Your Name
Course: CS 2430
Section: Your Section
Project: Programming Project 2
Semester: Your Semester

File Purpose:
This file contains all multiset (bag) operations using
Python's Counter class.
"""

from collections import Counter


# ----------------------------------------
# Print a multiset
# ----------------------------------------
def print_multiset(title, bag):

    print("--------------------------------------")
    print(title)
    print("--------------------------------------")

    if len(bag) == 0:
        print("Empty")
    else:
        for item in sorted(bag.keys()):
            print(f"{item}: {bag[item]}")

    print()


# ----------------------------------------
# Multiset Union
# Maximum count
# ----------------------------------------
def multiset_union(A, B):
    return A | B


# ----------------------------------------
# Multiset Intersection
# Minimum count
# ----------------------------------------
def multiset_intersection(A, B):
    return A & B


# ----------------------------------------
# Multiset Difference
# Subtract counts
# ----------------------------------------
def multiset_difference(A, B):
    return A - B


# ----------------------------------------
# Multiset Sum
# Add counts
# ----------------------------------------
def multiset_sum(A, B):
    return A + B


# ----------------------------------------
# Display all multiset operations
# ----------------------------------------
def run_multiset_operations(A, B):

    print("\n")
    print("======================================")
    print("PART 2 - MULTISET OPERATIONS")
    print("======================================\n")

    print_multiset("Multiset A", A)

    print_multiset("Multiset B", B)

    print_multiset(
        "Multiset Union",
        multiset_union(A, B)
    )

    print_multiset(
        "Multiset Intersection",
        multiset_intersection(A, B)
    )

    print_multiset(
        "Multiset Difference (A - B)",
        multiset_difference(A, B)
    )

    print_multiset(
        "Multiset Sum (A + B)",
        multiset_sum(A, B)
    )


# ----------------------------------------
# Sample Data
# ----------------------------------------
def create_sample_multisets():

    A = Counter({
        "Apple": 3,
        "Orange": 2,
        "Banana": 1,
        "Cherry": 2,
        "Mango": 1
    })

    B = Counter({
        "Apple": 1,
        "Orange": 4,
        "Pear": 2,
        "Cherry": 1,
        "Mango": 2
    })

    return A, B
