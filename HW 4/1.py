import copy

def special(arr):
    row = len(arr)
    col = len(arr[0])

    i = 0
    j = 0
    nop = []
    
    while i < (row - 1):
        while j < (col-1):
            if (not rb(arr,i,j)):
                nop.append([i,j])
            j += 1
        i += 1
        j = 0

    size = len(nop)

    if size > 2:
        print("Array is not suitable to convert special array.")
        return False

    elif size == 0:
        print("Array is a special array, no need to change any element.")

    elif size == 1:

        temp_arr =copy.deepcopy(arr)

        if correct( arr , nop[0][0] , nop[0][1] ):
            congratulations(temp_arr,arr)
            return True
        print("Array is not suitable to convert special array.")
        return False

    else:
        temp_arr =copy.deepcopy(arr)

        i1 = nop[0][0]
        j1 = nop[0][1]
        i2 = nop[1][0]
        j2 = nop[1][1]

        diff = max( ( arr[i1][j1] + arr[i1+1][j1+1] ) - ( arr[i1+1][j1] + arr[i1][j1+1] ) , ( arr[i2][j2] + arr[i2+1][j2+1] ) - ( arr[i2+1][j2] + arr[i2][j2+1] ) )

        if (( i2 - i1 ) == 1) and (( j2 - j1 ) == 1 ):

            if correct_location(arr,i2,j2,diff,False):
                congratulations(temp_arr,arr)
                return True
            print("Array is not suitable to convert special array.")
            return False

        elif (( i2 - i1 ) == 1) and (( j1 - j2 ) == 1 ):

            if correct_location(arr,i2,j1,diff,True):
                congratulations(temp_arr,arr)
                return True
            print("Array is not suitable to convert special array.")
            return False
        
        else:
            print("Array is not suitable to convert special array.")
            return False


def congratulations(temp_arr,arr):
    print("Array become specialized by only changing one element:")
    print("Old one:")
    for x in temp_arr:
        print(x)
    print("Specialized one:")
    for x in arr:
        print(x)

                
def correct_location(arr,i,j,diff,binary):
    if binary:
        real_diff = diff
    else:
        real_diff = -diff

    arr[i][j] += real_diff
    if (rb(arr,i,j) and ru(arr,i,j) and lu(arr,i,j) and lb(arr,i,j)):
        return True

    arr[i][j] -= real_diff
    return False


def correct(arr,i,j):
    diff = ( arr[i][j] + arr[i+1][j+1] ) - ( arr[i+1][j] + arr[i][j+1] )

    arr[i][j] -= diff

    if (rb(arr,i,j) and ru(arr,i,j) and lu(arr,i,j) and lb(arr,i,j)):
        return True

    arr[i][j] += diff
    try:
        arr[i][j+1] += diff
    except IndexError:
          pass

    if (rb(arr,i,j+1) and ru(arr,i,j+1) and lu(arr,i,j+1) and lb(arr,i,j+1)):
        return True

    try:
        arr[i][j+1] -= diff
    except IndexError:
        pass
    try:
        arr[i+1][j] += diff
    except IndexError:
        pass

    if (rb(arr,i+1,j) and ru(arr,i+1,j) and lu(arr,i+1,j) and lb(arr,i+1,j)):
        return True

    try:
        arr[i+1][j] -= diff
    except IndexError:
        pass
    try:
        arr[i+1][j+1] -= diff
    except IndexError:
        pass

    if (rb(arr,i+1,j+1) and ru(arr,i+1,j+1) and lu(arr,i+1,j+1) and lb(arr,i+1,j+1)):
        return True

    try:
        arr[i+1][j+1] += diff
    except IndexError:
        pass
    return False



#right_bottom
def rb(arr,i,j):
    try:
        if ( arr[i+1][j+1] + arr[i][j] ) <= ( arr[i][j+1] + arr[i+1][j] ):
            return True
    except IndexError:
        return True
    return False
#right_upside
def ru(arr,i,j):
    if (i-1) < 0:
        return True
    try:
        if ( arr[i-1][j] + arr[i][j+1] ) <= ( arr[i][j] + arr[i-1][j] ):
            return True
    except IndexError:
        return True
    return False
#left_upside
def lu(arr,i,j):
    if ((i-1) < 0) or ((j-1) < 0):
        return True
    if ( arr[i][j] + arr[i-1][j-1] ) <= ( arr[i-1][j] + arr[i][j-1] ):
        return True
    return False
#left_bottom
def lb(arr,i,j):
    if (j-1) < 0:
        return True
    try:
        if ( arr[i][j-1] + arr[i+1][j] ) <= ( arr[i][j] + arr[i+1][j-1] ):
            return True
    except IndexError:
        return True
    return False

T = [[10, 17, 13], 
     [17, 25, 16],
     [24, 28, 22]]


special(T)