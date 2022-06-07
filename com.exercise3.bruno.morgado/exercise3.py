'''
Student: Bruno Morgado
Student# 301-154-898
'''
import numpy as np

def build_array(array_range):
    # random index to remove from array
    rand_number = np.random.randint(1, array_range + 1)
    print(f'\nRandom Number: {rand_number}')

    full_array = np.arange(1, array_range + 1)
    print(f'\nFull array: {full_array}')
    incomplete_array = np.delete(full_array, np.where(full_array == rand_number))
    print(f'\nIncomplete array: {incomplete_array}')
    
    return incomplete_array

def find_missing_number(incomplete_array):
    
    length = len(incomplete_array) + 1
    total = (length*(length + 1)) / 2

    for i in range(len(incomplete_array)):
        total -= incomplete_array[i]
    
    return total



def main():
    
    print(f'\nTest with FIRST array')
    test_array1 = build_array(10)
    missing_num1 = find_missing_number(test_array1)
    print(f'Missing Number from test_array1 is: {missing_num1}')

    print('-'*100)

    print(f'\nTest with SECOND array')
    test_array2 = build_array(100)
    missing_num2 = find_missing_number(test_array2)
    print(f'\nMissing Number from test_array2 is: {missing_num2}')

    print('-'*100)

if __name__ == '__main__':

    main()
   