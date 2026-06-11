# ------------------------------- FUNCTIONS ----------------------------------   
def maximo(arr):
    if len(arr) == 1: # Base case
        return arr[0]
    resto_max = maximo(arr[1:]) # the rest of the maximum
    if arr[0] > resto_max:
        return arr[0]
    else:
        return resto_max

def binary_search(arr, item, low, high):
    if low > high: # base case: not found
        return -1
    
    mid = (low + high) // 2
    if arr[mid] == item: # base case: found
        return mid
    elif arr[mid] > item:
        return binary_search(arr, item, low, mid -1) # left
    else:
        return binary_search(arr, item, mid + 1, high) # right
    
def quicksort(array):
    if len(array) < 2:
        return array # Base case: arrays with 0 or 1 element are already sorted
    else:
        pivot = array[0] # Recursive case
        less = [i for i in array[1:] if i < pivot] #sub-array of all the elements less than the pivot
        greater = [i for i in array [1:] if i > pivot] # sub-array of all the elements greater than the pivot

        return quicksort(less) + [pivot]  + quicksort(greater)

# ----------------------------------------- TESTS --------------------------------------------- 
print("Testing  maximo...")
assert maximo([2, 32, 4, 51, 6, 43, 8, 15]) == 51
assert maximo([1]) == 1
assert maximo([10, 10]) == 10

print("Testing  binary search...")
assert binary_search([4, 67], 4 , 0 , 1) == 0
assert binary_search([1, 24, 58, 73], 15 , 0, 3) == -1 # no existe
assert binary_search([5, 11, 29, 38], 29, 0, 3) == 2 # encontrado en índice 2

print("Testing  quicksort...")
assert quicksort([83, 4, 54, 31]) == [4, 31, 54, 83]
assert quicksort([2, 15, 27, 39, 42]) == [2, 15, 27, 39, 42]
assert quicksort([45, 11]) ==  [11, 45]

print("✅ All tests passed!")