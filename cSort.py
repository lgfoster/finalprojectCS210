# Luke Foster
# Fall 2021 : CS - 210 Final Project 
#
# This project is a challenge to learn python from scratch and develop a counting sort. This sorting method is
# then timed and compared to the native list sort that exists in python3. 

import random
import time

# Handles the calls of both the list sort and counting sort. It generates a random array of one million ints
# with each cell being populated in a range of 0 to 100. 
def compareSorts():
    vector = [] * 1000000

    for i in vector:
        vector.append(random.randint(0,100))
        index = index + 1

    vector_L = listSort(vector)
    vector_C = counting(vector)

    # Determine if the vectors are equal
    notEqual = False

    for i in range(0, len(vector)):
        if(vector_C[i] != vector_L):
            notEqual = True

    if(notEqual):
        print("The sorted vectors are not equal\n")
    else:
        print("The sorted vectors are equal\n")


# This function calls the sort function that is native to the list data structure in python 3 and will
# display the time it takes for it to complete the sort
def listSort(vector):
    
    time_Start = time.perf_counter()

    vector.sort()

    time_Stop = time.perf_counter()

    print("Finished list sort in: ", time_Stop - time_Start)

    return vector

# This function is a wrapper function to c_Sort that will time the counting sort function
def counting(vector):

    time_Start = time.perf_counter()

    sorted = c_Sort(vector)

    time_Stop = time.perf_counter()

    print("Finished counting sort in: ", time_Stop - time_Start)

    return sorted

# Counting sort function that accepts the unsorted vector and then generates a new list that is properly
# sorted
def c_Sort(unsorted):

    counts = [0] * 101

    sorted = [] * 1000000

    # Count total occurences and sum counts with previous elements
    for index in range(0, len(unsorted)):
        counts[unsorted[index]] += 1

    for index in range(1, 101):
        counts[index] += counts[index - 1]

    index = len(unsorted) - 1
    while(index >= 0):
        sorted[counts[unsorted[index]] - 1] = unsorted[index]
        counts[unsorted[index]] -= 1
        index -= 1

    return sorted

# Main routine
compareSorts()