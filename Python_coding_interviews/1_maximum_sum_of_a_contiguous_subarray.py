# Function to find the maximum sum of a contiguous subarray
# in a given integer array
def solution(array):
    max_of_sum = 0 # stores the maximum sum sublist found so far
    max_ending = 0 # stores the maximum sum of sublist ending at the current position
    # traverse the given list
    for i in array:
        # update the maximum sum of sublist "ending" at index 'i' (by adding the
		# current element to maximum sum ending at previous index 'i-1')
        max_ending = max_ending + i
        # if the maximum sum is negative, set it to 0 (which represents
		# an empty sublist)
        max_ending = max(max_ending,0)
        # update the result if the current sublist sum is found to be greater
        max_of_sum = max(max_of_sum,max_ending)
    return max_of_sum

array = [-2, 100, -3, 4, -1, 2, 1, -5, 4]

print('The sum of contiguous sublist with the largest sum is',solution(array))