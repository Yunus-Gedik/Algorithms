import math

def wrapped(arr1, len1, arr2, len2, k):
    if (( len1 + len2 ) < k) or k == 0:
        print("There is not a k. element!")
        return
    elif ( len1 + len2 ) == k:
        return ( max( arr1[len1-1] , arr2[len2-1] ) )
    elif ( arr1[ len1-1 ] <= arr2[ math.floor( (len2 / 2) ) ] ) and (( len1 + math.floor( len2 / 2 )) >= k ):
        len2 = math.floor( len2 / 2 )
        return wrapped(arr1, len1, arr2, len2, k)
    elif ( arr2[ len2-1 ] <= arr1[ math.floor( (len1 / 2) ) ] ) and (( len2 + math.floor( len1 / 2 )) >= k ):
        len1 = math.floor( len1 / 2 )
        return wrapped(arr1, len1, arr2, len2, k)
    else:
        if arr1[ len1-1 ] > arr2[ len2-1 ]:
            len1 -= 1
        else:
            len2 -= 1
        return wrapped(arr1, len1, arr2, len2, k)

def kth(arr1, arr2, k):
    return wrapped(arr1, len(arr1) if len(arr1) < k else k, arr2, len(arr2) if len(arr2) < k else k, k)

arr1 = [12,23,32,41,57,64,75,97]
arr2 = [40,42,49,80,81,82,83,100]
k = 7
print(kth(arr1,arr2,k))