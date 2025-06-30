def two_sum(nums, target):
    # Create a dictionary to store the indices of the numbers we have seen
    num_indices = {}

    # Loop through the list
    for i, num in enumerate(nums):
        # Calculate the complement of the current number
        complement = target - num
        
        # Check if the complement is already in the dictionary
        if complement in num_indices:
            return [num_indices[complement], i]
        
        # If not, store the current number and its index in the dictionary
        num_indices[num] = i
    
    # Return an empty list if no solution is found
    return []


nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output: [0, 1] because nums[0] + nums[1] = 9
