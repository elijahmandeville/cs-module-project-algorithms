'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # Your code here

    # Sort the array
    arr.sort()

    # loop through the array (iterating by 2) and compare current num to next num
    for i in range(0, len(arr) - 1, 2):
        # if num is not equal to next num, return that num
        if arr[i] != arr[i+1]:
            return arr[i]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
