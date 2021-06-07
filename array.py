def arraysum(myList, sum):
    length = len(myList) - 1
    x = 0
    while(x < length):
        if(myList[x] + myList[x + 1] == sum):
            return [myList[x],myList[x + 1]]
        else:
            x = x + 1

array =  [2,7,11,15]
sum1 = 9
print(arraysum(array, sum1))
