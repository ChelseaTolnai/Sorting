# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = \
            arr[smallest_index], arr[cur_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swap = True
    while swap:
        # Step 4a - If no swaps performed, stop.
        swap = False
        # Step 1 - Loop through your array
        for i in range(0, len(arr) - 1):
            # Step 2 - Compare each element to its neighbor
            if arr[i] > arr[i+1]:
                # Step 3 - If elements in wrong position
                # (relative to each other, swap them)
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap = True
        # Step 4b - Else, go back to the element at index 0 and repeat step 1.
    return arr

"""
function countingSort(array, k) is
  count ← new array of k zeros
  for i = 1 to length(array) do
    count[array[i]] ← count[array[i]] + 1
  for i = 2 to k do
    count[i] ← count[i] + count[i - 1]
  for i = length(array) downto 1 do
    output[count[array[i]]] ← array[i]
    count[array[i]] ← count[array[i]] - 1
  return output
"""


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Find maximum range of count indexes
    for i in arr:
        # Find maximum number in list
        if i > maximum:
            maximum = i
        # Return error if any number is negative
        elif i < 0:
            return "Error, negative numbers not allowed in Count Sort"
    k = maximum+1

    # Set initial count of all numbers to zero
    count = [0 for i in range(k)]

    # Add to count for every number in list
    for i in arr:
        count[i] += 1

    # Modify count list to store previous sum of count
    for i in range(1, k):
        count[i] += count[i - 1]
    # The modified count list indicates the position of each number

    # Create temp list for swapping the num to correct position index
    temp_arr = [0 for i in range(len(arr))]
    # For every index place proper num into position
    # Then decrease count
    for i in range(len(arr)):
        temp_arr[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1
    arr = temp_arr
    return arr
