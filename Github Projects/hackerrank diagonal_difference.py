
array = [[9,6,5],[7,4,3],[1,8,2]]
x = int(array.split())
print(x)
def diagonal_difference(arr):
    sum = 0
    sum2 = 0
    var = len(arr) - 1
    for i in range(len(arr)):
        sum += arr[i][i]
        sum2 += arr[i][var]
        var -= 1

    return abs(sum - sum2)

#print(diagonal_difference(array))
    

