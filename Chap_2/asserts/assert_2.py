# ------------------------------------- FUNCTIONS --------------------------------------
def findSmallest(arr):
    smallest = arr[0] # Stores the smallest value
    smallest_index = 0 # Stores the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    copiedArr = list(arr) # copy array before mutating
    for i in range(len(copiedArr)):
        smallest = findSmallest(copiedArr)
        newArr.append(copiedArr.pop(smallest))
    return newArr

# ------------------------------------ TESTS -------------------------------------------

print("Testing findSmallest...")
assert findSmallest([15, 60, 7, 22, 8, 54]) == 2
assert findSmallest([37, 9, 42, 91, 2]) == 4
assert findSmallest([1]) == 0



print("Testing selectionSort...")
assert selectionSort([15, 60, 7, 22, 8, 54]) == [7, 8, 15, 22, 54, 60]
assert selectionSort([53, 96, 14, 0, 83, 3]) == [0, 3, 14, 53, 83, 96]
assert selectionSort([1]) == [1]
assert selectionSort([0, -1, -6]) == [-6, -1, 0]


print("✅ All tests passed!")