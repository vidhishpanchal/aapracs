# --------------------------WITHOUT COMMENTS---------------------
import random
def quicksort(arr, start , stop):
	if(start < stop):
		pivotindex = partitionrand(arr,start, stop)
		quicksort(arr , start , pivotindex-1)
		quicksort(arr, pivotindex + 1, stop)
def partitionrand(arr , start, stop):
	randpivot = random.randrange(start, stop)
	arr[start], arr[randpivot] = \
		arr[randpivot], arr[start]
	return partition(arr, start, stop)

def partition(arr,start,stop):
	pivot = start # pivot
	i = start + 1
	for j in range(start + 1, stop + 1):
		if arr[j] <= arr[pivot]:
			arr[i] , arr[j] = arr[j] , arr[i]
			i = i + 1
	arr[pivot] , arr[i - 1] = arr[i - 1] , arr[pivot]
	pivot = i - 1
	return (pivot)

# ---------------------------DRIVER CODE-----------------------
array = [10, 7, 8, 9, 1, 5]
quicksort(array, 0, len(array) - 1)
print(array)


















import random
print("------------RANDOMIZED QUICK SORT--------------")
def quicksort(arr, start, stop):
    if start<stop:
        pivotindex=partitionrand(arr, start, stop)
        quicksort(arr, start, pivotindex-1)
        quicksort(arr, pivotindex+1, stop)
 
#create random pivot and swap with start        
def partitionrand(arr, start, stop):
    randompivot=random.randrange(start, stop)
    print(f"random pivot : {arr[randompivot]}")
    arr[start], arr[randompivot]=arr[randompivot], arr[start]
    print("After swapping : ", arr)
    return partition(arr, start, stop)
    
#sort pivot acc to order
def partition(arr,start,stop):
    pivot = start # pivot
    i = start + 1
    print('-------------')
    for j in range(start + 1, stop + 1):
        if arr[j] <= arr[pivot]:
            arr[i] , arr[j] = arr[j] , arr[i]
            print(f'{arr[i]} and {arr[j]} are swapped')
            i = i + 1
        print(f"i = {i}; j={j}; {arr}")
    print('-------------')
    print('BEFORE:')
    print(f'arr[pivot] = {arr[pivot]}; arr[i - 1] = {arr[i - 1]}')
    arr[pivot] , arr[i - 1] = arr[i - 1] , arr[pivot]
    print('\nAFTER:')
    print(f'arr[pivot] = {arr[pivot]}; arr[i - 1] = {arr[i - 1]}')
    
    print(f'OLD pivot: {arr[pivot]}')
    pivot = i - 1
    print(arr)
    print("NEW pivot :", arr[pivot])
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    return (pivot)
            
            
array = [10, 7, 8, 9, 1, 5]
quicksort(array, 0, len(array) - 1)
print(array)
        









# -----------------------GFG CODE-------------
# Python implementation QuickSort using
# Lomuto's partition Scheme.
import random

'''
The function which implements QuickSort.
arr :- array to be sorted.
start :- starting index of the array.
stop :- ending index of the array.
'''
def quicksort(arr, start , stop):
	if(start < stop):
		
		# pivotindex is the index where
		# the pivot lies in the array
		pivotindex = partitionrand(arr,\
							start, stop)
		
		# At this stage the array is
		# partially sorted around the pivot.
		# Separately sorting the
		# left half of the array and the
		# right half of the array.
		quicksort(arr , start , pivotindex-1)
		quicksort(arr, pivotindex + 1, stop)

# This function generates random pivot,
# swaps the first element with the pivot
# and calls the partition function.
def partitionrand(arr , start, stop):

	# Generating a random number between the
	# starting index of the array and the
	# ending index of the array.
	randpivot = random.randrange(start, stop)

	# Swapping the starting element of
	# the array and the pivot
	arr[start], arr[randpivot] = \
		arr[randpivot], arr[start]
	return partition(arr, start, stop)

'''
This function takes the first element as pivot,
places the pivot element at the correct position
in the sorted array. All the elements are re-arranged
according to the pivot, the elements smaller than the
pivot is places on the left and the elements
greater than the pivot is placed to the right of pivot.
'''
def partition(arr,start,stop):
	pivot = start # pivot
	
	# a variable to memorize where the
	i = start + 1
	
	# partition in the array starts from.
	for j in range(start + 1, stop + 1):
		
		# if the current element is smaller
		# or equal to pivot, shift it to the
		# left side of the partition.
		if arr[j] <= arr[pivot]:
			arr[i] , arr[j] = arr[j] , arr[i]
			i = i + 1
	arr[pivot] , arr[i - 1] =\
			arr[i - 1] , arr[pivot]
	pivot = i - 1
	return (pivot)

# Driver Code
if __name__ == "__main__":
	array = [10, 7, 8, 9, 1, 5]
	quicksort(array, 0, len(array) - 1)
	print(array)


















# This code is contributed by soumyasaurav


# ------------RANDOMIZED QUICK SORT--------------
# random pivot : 1
# After swapping :  [1, 7, 8, 9, 10, 5]
# -------------
# i = 1; j=1; [1, 7, 8, 9, 10, 5]
# i = 1; j=2; [1, 7, 8, 9, 10, 5]
# i = 1; j=3; [1, 7, 8, 9, 10, 5]
# i = 1; j=4; [1, 7, 8, 9, 10, 5]
# i = 1; j=5; [1, 7, 8, 9, 10, 5]
# -------------
# BEFORE:
# arr[pivot] = 1; arr[i - 1] = 1

# AFTER:
# arr[pivot] = 1; arr[i - 1] = 1
# OLD pivot: 1
# [1, 7, 8, 9, 10, 5]
# NEW pivot : 1
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# random pivot : 10
# After swapping :  [1, 10, 8, 9, 7, 5]
# -------------
# 8 and 8 are swapped
# i = 3; j=2; [1, 10, 8, 9, 7, 5]
# 9 and 9 are swapped
# i = 4; j=3; [1, 10, 8, 9, 7, 5]
# 7 and 7 are swapped
# i = 5; j=4; [1, 10, 8, 9, 7, 5]
# 5 and 5 are swapped
# i = 6; j=5; [1, 10, 8, 9, 7, 5]
# -------------
# BEFORE:
# arr[pivot] = 10; arr[i - 1] = 5

# AFTER:
# arr[pivot] = 5; arr[i - 1] = 10
# OLD pivot: 5
# [1, 5, 8, 9, 7, 10]
# NEW pivot : 10
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# random pivot : 9
# After swapping :  [1, 9, 8, 5, 7, 10]
# -------------
# 8 and 8 are swapped
# i = 3; j=2; [1, 9, 8, 5, 7, 10]
# 5 and 5 are swapped
# i = 4; j=3; [1, 9, 8, 5, 7, 10]
# 7 and 7 are swapped
# i = 5; j=4; [1, 9, 8, 5, 7, 10]
# -------------
# BEFORE:
# arr[pivot] = 9; arr[i - 1] = 7

# AFTER:
# arr[pivot] = 7; arr[i - 1] = 9
# OLD pivot: 7
# [1, 7, 8, 5, 9, 10]
# NEW pivot : 9
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# random pivot : 8
# After swapping :  [1, 8, 7, 5, 9, 10]
# -------------
# 7 and 7 are swapped
# i = 3; j=2; [1, 8, 7, 5, 9, 10]
# 5 and 5 are swapped
# i = 4; j=3; [1, 8, 7, 5, 9, 10]
# -------------
# BEFORE:
# arr[pivot] = 8; arr[i - 1] = 5

# AFTER:
# arr[pivot] = 5; arr[i - 1] = 8
# OLD pivot: 5
# [1, 5, 7, 8, 9, 10]
# NEW pivot : 8
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# random pivot : 5
# After swapping :  [1, 5, 7, 8, 9, 10]
# -------------
# i = 2; j=2; [1, 5, 7, 8, 9, 10]
# -------------
# BEFORE:
# arr[pivot] = 5; arr[i - 1] = 5

# AFTER:
# arr[pivot] = 5; arr[i - 1] = 5
# OLD pivot: 5
# [1, 5, 7, 8, 9, 10]
# NEW pivot : 5
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# [1, 5, 7, 8, 9, 10]
# > 
        
        
        
        