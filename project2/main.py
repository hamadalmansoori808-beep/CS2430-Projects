"""
Name: Your Name
Course: CS 2430
Section: Your Section
Project: Programming Project 2
Semester: Your Semester

File Purpose:
Main program for Programming Project 2.
Runs all ordinary set operations and multiset operations.
"""

from collections import Counter

from set_operations import run_set_operations
from multiset_operations import (
    run_multiset_operations,
    create_sample_multisets
)


# ----------------------------------------
# Test Case 1
# Normal Sets
# ----------------------------------------
def test_case_1():

    print("\n")
    print("############################################")
    print("TEST CASE 1 - NORMAL SETS")
    print("############################################")

    A = {
        "Apple",
        "Orange",
        "Mango",
        "Cherry"
    }

    B = {
        "Orange",
        "Pear",
        "Kiwi",
        "Cherry"
    }

    run_set_operations(A, B)


# ----------------------------------------
# Test Case 2
# No Common Elements
# ----------------------------------------
def test_case_2():

    print("\n")
    print("############################################")
    print("TEST CASE 2 - NO COMMON ELEMENTS")
    print("############################################")

    A = {
        "Apple",
        "Banana",
        "Mango"
    }

    B = {
        "Pear",
        "Kiwi",
        "Cherry"
    }

    run_set_operations(A, B)


# ----------------------------------------
# Test Case 3
# Edge Case
# Empty Set
# ----------------------------------------
def test_case_3():

    print("\n")
    print("############################################")
    print("TEST CASE 3 - EMPTY SET")
    print("############################################")

    A = set()

    B = {
        "Apple",
        "Banana",
        "Cherry"
    }

    run_set_operations(A, B)


# ----------------------------------------
# Multiset Test
# ----------------------------------------
def multiset_test():

    print("\n")
    print("############################################")
    print("MULTISET TEST")
    print("############################################")

    A, B = create_sample_multisets()

    run_multiset_operations(A, B)


# ----------------------------------------
# Main
# ----------------------------------------
def main():

    print("=" * 60)
    print("CS2430 - PROGRAMMING PROJECT 2")
    print("SET OPERATIONS")
    print("=" * 60)

    test_case_1()

    test_case_2()

    test_case_3()

    multiset_test()

    print("\n")
    print("=" * 60)
    print("PROGRAM FINISHED")
    print("=" * 60)


if __name__ == "__main__":
    main()
