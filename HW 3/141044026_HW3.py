import math
from itertools import combinations

# Globals
swap_count_qs = 0
swap_count_is = 0


# Question 1
def _2n(arr):
    i = 1
    j = int(len(arr) / 2)
    endpoint = j
    if j % 2 != 0:
        j += 1

    while i < endpoint:
        if arr[i-1].lower() == "black":
            swap(arr,i,j)
            j += 2
            i += 2

def swap(arr,i,j):
    arr[i],arr[j] = arr[j],arr[i]

# Question 2

def fakecoin(arr):
    i = 0
    while i+1 < len(arr):
        if arr[i] == arr[i+1]:
            i += 1
            continue
        else:
            if i != 0:
                if arr[i-1] == arr[i]:
                    return arr[i+1]
                else:
                    return arr[i]
            else:
                if arr[i+1] == arr[i+2]:
                    return arr[i]
                else:
                    return arr[i+1]
        i += 1


# Question 3

# Insertion Sort
def insertionSort(arr): 
    global swap_count_is
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
            swap_count_is += 1
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = key 

# Quick Sort
def partition(arr,low,high): 
    global swap_count_qs
    i = ( low-1 )        
    pivot = arr[high]     

    for j in range(low , high): 
        if   arr[j] <= pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
            swap_count_qs += 1
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    swap_count_qs += 1
    return ( i+1 ) 

def quickSort(arr,low,high):

    if low < high:
        p = partition(arr,low,high) 
        quickSort(arr, low, p-1) 
        quickSort(arr, p+1, high) 


# Question 4

# Main solution for question 4 using insertion sort
def median_is(arr):
    insertionSort(arr)
    if len(arr) % 2 == 0:
        return (arr[int(len(arr)/2)] + float(arr[int(len(arr)/2) - 1])) / 2
    else:
        return arr[int(math.floor(len(arr)/2))]

# For practise I made a alternative solution using selection sort
def median_ss(arr):
    half_selection_sort(arr)
    if len(arr) % 2 == 0:
        return (arr[int(len(arr)/2)] + float(arr[int(len(arr)/2 - 1)])) / 2
    else:
        return arr[int(math.floor(len(arr)/2))]

def half_selection_sort(arr):
    for i in range(int(len(arr)/2)+1): 
        min_idx = i 
        for j in range(i+1, len(arr)): 
            if arr[min_idx] > arr[j]: 
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i] 


# Question 5

def sub_lister(my_list):
	subs = []
	for i in range(0, len(my_list)+1):
	  temp = [list(x) for x in combinations(my_list, i)]
	  if len(temp)>0:
	    subs.extend(temp)
	return subs

def optimal_sublist(arr):
    the_value = (max(arr) + min(arr)) * len(arr) / 4
    sublists = sub_lister(arr)
    cleanlist = []

    # Get rid of unacceptable sublists.
    for sublist in sublists:
        if sum(sublist) >= the_value:
            cleanlist.append(sublist)

    sublists = cleanlist[:]

    # Find minimum length of among acceptable lists.
    min_len = len(sublists[0])
    for sublist in sublists:
        if len(sublist) < min_len:
            min_len = len(sublist)

    # Discard longer lists according to minimum length.
    for sublist in sublists:
        if len(sublist) > min_len:
            cleanlist.remove(sublist)

    sublists = cleanlist[:]

    #Find most optimal sublists' index among minimum lengthed acceptable lists. 
    min_value = sum(sublists[0])
    min_index = 0
    i = 0
    for sublist in sublists:
        if sum(sublist) < min_value:
            min_value = sum(sublist)
            min_index = i
        i += 1

    return sublists[min_index]
    


# Driver function

def driver():
# Question 1
    print("Question 1\n")
    thislist = ["black", "black", "black", "black", "black","white","white" ,"white", "white", "white"]
    print("Before: ")
    print(thislist)
    _2n(thislist)
    print("After: ")
    print(thislist)

    print("")

    thislist = ["black", "black", "black", "black", "white", "white", "white","white"]
    print("Before: ")
    print(thislist)
    _2n(thislist)
    print("After: ")
    print(thislist)

# Question 2
    print("\nQuestion 2\n")
    arr = [1,2,1]
    print(arr)
    print(fakecoin(arr))

    print("")

    arr = [3,3,3,3,3,3,3,7,3,3,3,3]
    print(arr)
    print(fakecoin(arr))

# Question 3 quick sort
    print("\nQuestion 3 quick sort\n")
    arr = [3,9,11,8,7,4]
    print("Before: ")
    print(arr)
    quickSort(arr,0,len(arr)-1)
    print("After: ")
    print(arr)
    print("Swap count is quick sort : %d" %(swap_count_qs))

# Question 3 insertion sort
    print("\nQuestion 3 insertion sort\n")
    arr = [3,9,11,8,7,4]
    print("Before: ")
    print(arr)
    insertionSort(arr) 
    print("After: ")
    print(arr)
    print("Swap count is insertion sort : %d" %(swap_count_is))

# Question 4 main solution test
    print("\nQuestion 4 main solution test\n")
    arr = [64, 25, 12, 23, 11,3] 
    print("Median : %f" %(median_is(arr)))
    print(arr)

    arr = [64, 25, 12, 23, 11,3,5] 
    print("Median : %f" %(median_is(arr)))
    print(arr)

# Question 4 alternative solution test
    print("\nQuestion 4 alternative solution test\n")
    arr = [64, 25, 12, 23, 11,3] 
    print("Median : %f" %(median_ss(arr)))
    print(arr)

    arr = [64, 25, 12, 23, 11,3,5] 
    print("Median : %f" %(median_ss(arr)))
    print(arr)

# Question 5
    print("\nQuestion 5\n")
    l1 = [10, 20, 30,40,50]
    print("List:")
    print(l1)
    print("")
    print("Sublists:")
    print(sub_lister(l1))
    print("")
    print("Optimal:")
    print(optimal_sublist(l1))

driver()