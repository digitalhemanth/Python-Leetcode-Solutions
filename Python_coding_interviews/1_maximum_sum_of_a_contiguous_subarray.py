# Function to find the maximum sum of a contiguous subarray
# in a given integer array

def solution(array):
    
    max_of_sum = 0
    max_ending = 0
    
    for i in array:
        max_ending = max_ending + i
        max_ending = max(max_ending,0)
        max_of_sum = max(max_of_sum,max_ending)
    
    return max_of_sum

array = [-2, 100, -3, 4, -1, 2, 1, -5, 4]
print(solution(array))