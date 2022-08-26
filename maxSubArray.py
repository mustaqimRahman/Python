


def max_sub_array_of_size_k(k, arr):
  # TODO: Write your code here
  maxsum=0
  result = []
  for windowstart in range (len(arr)-k+1):
    result = arr[windowstart:windowstart+k]
    print(result)
    listsum = sum(result)
    print(listsum)
    if listsum> maxsum:
      maxsum = listsum
    print(maxsum)

  


max_sub_array_of_size_k(3, [2, 1, 5, 1, 3,2])