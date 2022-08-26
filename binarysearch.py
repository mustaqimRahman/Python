import math

def binary_search(s,arr):
    arr.sort()
    median = (len(arr)//2)
    flag = False
    while flag == False:
        # if the number is equal to the median value
        if arr[median]==s:
            result = arr[median]
            flag= True
        # if the number is greater than the median value    
        elif arr[median]<s:
            arr = arr[median+1:]
            median = (len(arr)//2)
        # if the number is smaller than the median value
        elif arr[median]>s:
            arr = arr[:median]
            median = (len(arr)//2)

    print(arr)
    print(result)


binary_search(5,[10,5,3,6,4,7,9])
binary_search(5,[10,5,3,6,4,7,9])