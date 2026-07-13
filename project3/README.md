# Programming Project 3 - The Knapsack Problem

## Course

CS 2430

## Programming Language

Python 3.x

## Project Description

This project implements different strategies to solve the 0/1 Knapsack Problem.
The goal is to select the best combination of science experiments while keeping
the total payload weight at or below 700 kg.

The project compares:

- Three greedy strategies
- Brute-force exhaustive search
- Dynamic Programming solution

---

# Files

## main.py

Main program that stores experiment data and runs all algorithms.

## greedy.py

Contains three greedy approaches:

1. Highest Rating First
2. Lightest Weight First
3. Best Rating-to-Weight Ratio First

## brute_force.py

Generates all possible experiment combinations (2^12 = 4096)
and finds the top three valid solutions.

## dp.py

Contains the Dynamic Programming implementation of the
0/1 Knapsack problem.

---

# Requirements

Python 3.x

No external libraries are required.

---

# How to Run

Open the project3 folder.

Run:

```bash
python main.py
