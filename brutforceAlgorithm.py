#count the sym of 5 consecutive elements in an array

# generic solution with complexity O(N*K)

def find_avg_of_subarray(array,k):
    result =[]
    for i in range(len(array)-k+1):
        _sum = 0.0
        for j in range (i,i+k):
            _sum += array[j]

        result.append(_sum/k)
    return result





## Sliding window approach to the problem 

def find_averages_of_subarrays_slidingWindow(arr,K):
  result = []
  windowSum, windowStart = 0.0, 0
  for windowEnd in range(len(arr)):
    print(windowEnd)
    windowSum += arr[windowEnd]  # add the next element
    # slide the window, we don't need to slide if we've not hit the required window size of 'k'
    if windowEnd >= K - 1:
      result.append(windowSum / K)  # calculate the average
      windowSum -= arr[windowStart]  # subtract the element going out
      windowStart += 1  # slide the window ahead

  return result





def main():
    array = [1, 3, 2, 6, -1, 4, 1, 8, 2] 
    k=5
    # response = find_avg_of_subarray(array,k)
    response = find_averages_of_subarrays_slidingWindow(array,k)

    print("The avg sum of 5 consecutive elements in the array are: " + str(response))

main()


