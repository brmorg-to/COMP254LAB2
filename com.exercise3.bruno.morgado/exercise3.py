'''
Student: Bruno Morgado
Student# 301-154-898
'''


'''
An array A contains n−1 unique integers in the range [0,n−1], that is, there is one number from this range that is not in A.
Design an O(n)-time algorithm for finding that number. You are only allowed to use O(1) additional space besides the array A itself.
Write the java method that implements this algorithm and a main method to test it.
Hint: Numbers in [0, n-1] form an arithmetic progression whose sum is known.
'''
# Import required modules / libraries
import numpy as np

# Build an array with a missing number based on a range value.
def build_array(array_range):
    # random index to remove from array
    rand_number = np.random.randint(1, array_range + 1)
    print(f'\nRandom Number: {rand_number}')

    full_array = np.arange(1, array_range + 1)
    print(f'\nFull array: {full_array}')
    incomplete_array = np.delete(full_array, np.where(full_array == rand_number))
    print(f'\nIncomplete array: {incomplete_array}')
    
    return incomplete_array

# Identifies the missing number in the array
def find_missing_number(incomplete_array):
    
    length = len(incomplete_array) + 1
    # Calculate the sum of all values in a complete array
    total = (length*(length + 1)) / 2

    # Iterate through the incomplete array and subtract its values from the total
    for i in range(len(incomplete_array)):
        total -= incomplete_array[i]
    
    # Return the missing number
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
   