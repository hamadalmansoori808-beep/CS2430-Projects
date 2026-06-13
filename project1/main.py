# Hamad Almansoori
# CS 2430
# Programming Project 1
# Summer 2026
# Main program for sorting algorithm comparison

import random

# -----------------------------
# Merge Sort
# -----------------------------
def merge_sort(arr):
    comparisons = [0]

    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            comparisons[0] += 1
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def sort(a):
        if len(a) <= 1:
            return a

        mid = len(a) // 2
        left = sort(a[:mid])
        right = sort(a[mid:])

        return merge(left, right)

    return sort(arr.copy()), comparisons[0]


# -----------------------------
# Quick Sort
# -----------------------------
def quick_sort(arr):
    comparisons = [0]

    def sort(a):
        if len(a) <= 1:
            return a

        pivot = a[len(a)//2]
        left = []
        middle = []
        right = []

        for x in a:
            comparisons[0] += 1
            if x < pivot:
                left.append(x)
            elif x > pivot:
                right.append(x)
            else:
                middle.append(x)

        return sort(left) + middle + sort(right)

    return sort(arr.copy()), comparisons[0]


# -----------------------------
# Heap Sort
# -----------------------------
def heap_sort(arr):
    a = arr.copy()
    comparisons = [0]

    def heapify(n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            comparisons[0] += 1
            if a[left] > a[largest]:
                largest = left

        if right < n:
            comparisons[0] += 1
            if a[right] > a[largest]:
                largest = right

        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            heapify(n, largest)

    n = len(a)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(i, 0)

    return a, comparisons[0]


# -----------------------------
# Shaker Sort
# -----------------------------
def shaker_sort(arr):
    a = arr.copy()
    comparisons = 0

    left = 0
    right = len(a) - 1

    while left < right:

        for i in range(left, right):
            comparisons += 1
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]

        right -= 1

        for i in range(right, left, -1):
            comparisons += 1
            if a[i] < a[i - 1]:
                a[i], a[i - 1] = a[i - 1], a[i]

        left += 1

    return a, comparisons


# -----------------------------
# Dataset Generator
# -----------------------------
def generate_data(n):
    return random.sample(range(1, 100), n)


# -----------------------------
# Test Driver
# -----------------------------
sizes = [4, 6, 8]

for n in sizes:

    data = generate_data(n)

    print("\n===================================")
    print("Array Size:", n)
    print("Original Array:", data)

    sorted_data, count = merge_sort(data)
    print("\nMerge Sort")
    print("Sorted:", sorted_data)
    print("Comparisons:", count)

    sorted_data, count = quick_sort(data)
    print("\nQuick Sort")
    print("Sorted:", sorted_data)
    print("Comparisons:", count)

    sorted_data, count = heap_sort(data)
    print("\nHeap Sort")
    print("Sorted:", sorted_data)
    print("Comparisons:", count)

    sorted_data, count = shaker_sort(data)
    print("\nShaker Sort")
    print("Sorted:", sorted_data)
    print("Comparisons:", count)
