"""
Name: hamad almansoori
Course: CS 2430
Project: Programming Project 2
Semester: Summer 2026

File Purpose:
This file contains all ordinary set operations using
Python sets and displays both element names and bit strings.
"""

# Universal set (10 elements)
UNIVERSAL_SET = [
    "Apple",
    "Banana",
    "Orange",
    "Mango",
    "Pear",
    "Peach",
    "Grapes",
    "Kiwi",
    "Lemon",
    "Cherry"
]


# ----------------------------------------
# Convert a set to a bit string
# ----------------------------------------
def bit_string(my_set):
    bits = []

    for item in UNIVERSAL_SET:
        if item in my_set:
            bits.append("1")
        else:
            bits.append("0")

    return "".join(bits)


# ----------------------------------------
# Print a set and its bit string
# ----------------------------------------
def print_set(title, my_set):

    print("--------------------------------------")
    print(title)
    print("--------------------------------------")

    print("Elements:")
    print(sorted(my_set))

    print("Bit String:")
    print(bit_string(my_set))
    print()


# ----------------------------------------
# Complement
# ----------------------------------------
def complement(A):
    return set(UNIVERSAL_SET) - A


# ----------------------------------------
# Union
# ----------------------------------------
def union(A, B):
    return A | B


# ----------------------------------------
# Intersection
# ----------------------------------------
def intersection(A, B):
    return A & B


# ----------------------------------------
# Difference
# ----------------------------------------
def difference(A, B):
    return A - B


# ----------------------------------------
# Symmetric Difference
# ----------------------------------------
def symmetric_difference(A, B):
    return A ^ B


# ----------------------------------------
# Display all ordinary set operations
# ----------------------------------------
def run_set_operations(A, B):

    print("\n")
    print("======================================")
    print("PART 1 - ORDINARY SET OPERATIONS")
    print("======================================\n")

    print("Universal Set")
    print(UNIVERSAL_SET)
    print()

    print_set("Set A", A)
    print_set("Set B", B)

    print_set("NOT(A)", complement(A))

    print_set("A UNION B", union(A, B))

    print_set("A INTERSECTION B", intersection(A, B))

    print_set("A - B", difference(A, B))

    print_set("A SYMMETRIC DIFFERENCE B",
              symmetric_difference(A, B))
