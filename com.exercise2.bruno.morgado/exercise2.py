'''
Student: Bruno Morgado
Student# 301-154-898
'''

'''
Perform an experimental analysis of the two algorithms prefixAverage1 and prefixAverage2, from lesson examples.
Optionally, visualize their running times as a function of the input size with a log-log chart. 
Use either Java or Python graphical capabilities for visualization. 
Hint: Choose representative values of the input size n, similar to StringExperiment.java from class examples.
'''

# Import the necessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from multiprocessing import Pool, cpu_count
import concurrent.futures
from time import perf_counter, perf_counter_ns
import seaborn as sns
import os

# First method to be tested. O(n^2) time complexity
def prefix_average1(array_x):
    n = len(array_x)
    a = [0] * n

    for j in range(n):
        total = 0.0;
        for i in range(j+1):
            total += array_x[i]

        a[j] = total / (j + 1.0);

    return a;

#Second method to be tested. O(n) time complexity
def prefix_average2(array_x):
    n = len(array_x)
    a = [0] * n
    total = 0.0

    for  j in range(n):
        total += array_x[j];
        a[j] = total / (j + 1.0);
    return a;

# Method to return the time that prefix1 spends to process a given array
def prefix1_time(array):
    print(f'\nLength of array = {len(array)}')
    start = perf_counter()
    prefix_average1(array)
    stop = perf_counter()
    print(f"[Process ID]:{os.getpid()} ...")
    time = stop - start
    print(f'Time Prefix1: {time}')
    #return the time in seconds
    return time

# Method to return the time that prefix2 spends to process a given array
def prefix2_time(array):
    print(f'\nLength of array = {len(array)}')
    start = perf_counter()
    prefix_average2(array)
    stop = perf_counter()
    print(f"[Process ID]:{os.getpid()} ...")
    time = stop - start
    print(f'Time Prefix2: {time}')
    #return the time in seconds
    return time

# Loglog plot of array sizes versus processing time for the two methods under analysis
def plot_loglog(x, y1, y2):

    fig, ax = plt.subplots(figsize=[11, 7])
    ax.loglog(x, y1, ':b', linewidth=2)
    ax.loglog(x, y2, '--r', linewidth=2)
    ax.set_title('loglog prefix1 O(n^2) / prefisx2 O(n)  ', fontsize=15)
    ax.set_xlabel('Aray Length', fontsize=13)
    ax.set_ylabel('Time', fontsize=13)
    ax.legend(['O(n^2)', 'O(n)'])
    plt.show()

# Method to start the experimental analysis, print the times arrays and plot the lolog graph.
# This method can be run via single or multi processing
def process_analysis(list_of_arrays):

    '''Single processing'''
    # list_times1 = []
    # for array in list_of_arrays:
    #     time = prefix1_time(array)
    #     list_times1.append(time)

    # list_times2 = []
    # for array in list_of_arrays:
    #     time = prefix2_time(array)
    #     list_times2.append(time)

    '''An alternative approach to run it with multiprocessing'''
    with concurrent.futures.ProcessPoolExecutor() as executor:
        list_times1 = [x for x in (executor.map(prefix1_time, list_of_arrays))]
        list_times2 = [x for x in (executor.map(prefix2_time, list_of_arrays))]
    # Print the resulting list of times that the methods took to process the list of arrays
    print(list_times1)
    print(f'\n{list_times2}')

    x = [len(array) for array in(list_of_arrays)]
    y1 = list_times1
    y2 = list_times2
    #Plot loglog Graph
    plot_loglog(x, y1, y2)


def main():

    LIST_ARRAYS = []
    
    for i in range(10001, 110000, 10000):
        LIST_ARRAYS.append(np.arange(1, i, 1))

    process_analysis(LIST_ARRAYS)


if __name__ == '__main__':

    main()
