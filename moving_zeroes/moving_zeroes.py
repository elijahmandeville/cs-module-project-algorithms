'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here

    # loop through arr
    for i in range(0, len(arr)):
        # if num at current index is 0, remove that 0, and append a 0 to the end
        if arr[i] == 0:
            arr.remove(arr[i])
            arr.append(0)
    # return the new arr
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 0, 0, 0, 3, 2, 1]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
