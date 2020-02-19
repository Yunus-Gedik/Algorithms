#Algorithm HW 5
#141044026
#Yunus Gedik

def opt_1(m,nar,sar):
    if len(nar) == 0:
        return 0

    return min( ny(m,nar,sar) , sf(m,nar,sar) )

def ny(m,nar,sar):
    i = len(nar)
    if i == 0:
        return 0

    return nar[i-1] + min( ny( m , nar[0:(i-1)] , sar[0:(i-1)] ) , m + sf( m , nar[0:(i-1)] , sar[0:(i-1)] ) )

def sf(m,nar,sar):
    i = len(nar)
    if i == 0:
        return 0

    return sar[i-1] + min( sf( m , nar[0:(i-1)] , sar[0:(i-1)] ) , m + ny( m , nar[0:(i-1)] , sar[0:(i-1)] ) )


def second(x): 
    return x[1]

def opt_2(arr):
    arr.sort(key = second)

    time = -1

    print("Selected sessions:")
    for x in arr:
        if x[0] >= time:
            time = x[1]
            print(x)


def opt_4(seq1,seq2,n,m,k):
    cost = 0
    for i in range(0,len(seq1)):
        if seq1[i] == seq2[i]:
            cost += n
        else:
            cost += m
    return cost


def opt_5(arr):
    oper = 0
    arr.sort()

    summ = arr[0]

    i = 1
    while i < len(arr):
        oper += summ + arr[i]
        summ += arr[i]
        i += 1

    return oper


def driver():
    newyork      = [1,17,26,20]
    sanfrancisco = [1,30,5,26]
    print("Question 1:")
    print()
    print("Newyork ")
    print(newyork)
    print("San Francisco")
    print(sanfrancisco)
    print("Result is:")
    print( opt_1( 10 , newyork , sanfrancisco ) )

    print()
    print("Question 2:")
    print()
    arr = [[1,3],[1,2],[1,4],[2,7],[3,4],[4,5]]
    print("Sessions are:")
    print(arr)
    opt_2(arr)

    print()
    print("Question 4:")
    print()
    a = "yunus"
    b = "yanis"
    print(a)
    print(b)
    print("Match cost: %d Mismatch cost: %d Gap cost %d"%(3,2,1))
    print("Cost is: %d"%(opt_4(a,b,3,2,1)))

    print()
    print("Question 5:")
    print()
    arr =[7,2,3,4,5]
    print(arr)
    print("Number of operations: %d"%(opt_5(arr)))

driver()