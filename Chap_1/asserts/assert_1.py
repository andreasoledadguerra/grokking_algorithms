# ------------------------- TESTS --------------------------------------
print("Testing binary_search...")

def binary_search(arr, item):
    assert arr == sorted(arr), "binary_search required a sorted list"
    low = 0
    high = len(arr)-1 # low and high keep track of which part of the list you'll search in

    while low <= high: # while you haven't narrowed it down to one element
        mid = (low + high) // 2 # Check the middle element
        guess = arr[mid]
        if guess == item: # Found the item
            return mid
        elif guess > item: # The guess was too high
            high = mid - 1
        else:              # The guess was too low
            low = mid + 1
    return None            # The item doesn't exist


my_list = [8, 15, 22, 32, 45, 50]

assert binary_search(my_list, 8) == 0, "First element" 
assert binary_search(my_list, 50) == 5, "Last element"
assert binary_search(my_list, 22) == 2, "Middle element" 

assert binary_search(my_list, 13) is None, "Not in list"
assert binary_search(my_list, -74) is None, "Negative number, not in list"
assert binary_search(my_list, 60) is None, "Out of range"

print(" ✅ All tests passed ")

