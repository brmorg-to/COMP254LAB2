'''
Student: Bruno Morgado
Student# 301-154-898
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from multiprocessing import Pool, cpu_count
import concurrent.futures
from time import perf_counter
import seaborn as sns
import os


def prefix_average1(array_x):
    n = len(array_x)
    a = [0] * n

    for j in range(n):
        total = 0.0;
        for i in range(j+1):
            total += array_x[i]

        a[j] = total / (j + 1.0);

    return a;

def prefix_average2(array_x):
    n = len(array_x)
    a = [0] * n
    total = 0.0

    for  j in range(n):
        total += array_x[j];
        a[j] = total / (j + 1.0);
    return a;


def prefix1_time(array):
    print(f'Length of array = {len(array)}')
    start = perf_counter()
    prefix_average1(array)
    stop = perf_counter()
    print(f"[Process ID]:{os.getpid()} ...")
    time = stop - start
    print(f'Prefix1: {time}\n')

    return time


def prefix2_time(array):
    print(f'Length of array = {len(array)}')
    start = perf_counter()
    prefix_average2(array)
    stop = perf_counter()
    print(f"[Process ID]:{os.getpid()} ...")
    time = stop - start
    print(f'Prefix2: {time}\n')
    
    return time


def plot_loglog(x, y1, y2):

    # data1 = pd.DataFrame({'Array Size': x, 'Time': y1})
    # data2 = pd.DataFrame({'Array Size': x, 'Time': y2})

    # Creating figure and axes
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=[7, 11])


    # Plotting the graph with Log ticks at x and y axis using loglog
    ax1.loglog(x, y1, ':b', linewidth=2)
    ax1.set_title('loglog plot O(n^2)', fontsize=15)
    ax1.set_xlabel('Aray Length', fontsize=13)
    ax1.set_ylabel('Time', fontsize=13)

    ax2.loglog(x, y2, '--r', linewidth=2)
    ax2.set_title('loglog plot O(n)', fontsize=15)
    ax2.set_xlabel('Array Length', fontsize=13)
    ax2.set_ylabel('Time', fontsize=13)

    plt.tight_layout()
    plt.show()


def process_analysis(list_of_arrays):

    '''Single processing'''
    list_times1 = []
    for array in list_of_arrays:
        time = prefix1_time(array)
        list_times1.append(time)

    list_times2 = []
    for array in list_of_arrays:
        time = prefix2_time(array)
        list_times2.append(time)


    '''An alternative approach to run it with multiprocessing'''
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     list_times1 = [x for x in (executor.map(prefix1_time, list_of_arrays))]
    #     list_times2 = [x for x in (executor.map(prefix2_time, list_of_arrays))]
    

    print(list_times1)
    print(f'\n{list_times2}')

    x = [len(array) for array in(list_of_arrays)]
    y1 = list_times1
    y2 = list_times2

    plot_loglog(x, y1, y2)


def main():

    LIST_ARRAYS = []
    
    for i in range(10001, 101000, 10000):
        LIST_ARRAYS.append(np.arange(1, i, 1))

    process_analysis(LIST_ARRAYS)

    # print(LIST_ARRAYS)


if __name__ == '__main__':

    main()

