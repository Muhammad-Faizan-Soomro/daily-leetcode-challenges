# Problem: 3005. Count Elements With Maximum Frequency
# Task:
# - Given a list of integers, find the sum of frequencies of the elements that appear most frequently.
#
# Example:
#   nums = [1, 2, 2, 3, 1, 4]
#   Frequencies = {1:2, 2:2, 3:1, 4:1}
#   Max frequency = 2
#   Elements with max frequency = [1, 2]
#   Answer = 2 (freq of 1) + 2 (freq of 2) = 4
#
# Approach:
# 1. Build a frequency map of all numbers.
# 2. Use an array of lists (buckets) to group numbers by frequency.
# 3. Traverse buckets from highest → lowest frequency.
# 4. When we find the highest frequency bucket with elements, return frequency * number of elements.
#
# Time Complexity: O(n)   -> counting + traversing once
# Space Complexity: O(n)  -> hashmap + bucket array of size n+1

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # Create a list of empty lists (buckets), index = frequency
        arr = [[] for _ in range(len(nums) + 1)]

        # Step 1: Count frequency of each element
        count_map = {}
        for num in nums:
            if num in count_map:
                count_map[num] = count_map[num] + 1
            else:
                count_map[num] = 1

        # Step 2: Place elements into buckets based on their frequency
        for k, v in count_map.items():
            arr[v].append(k)

        # Step 3: Traverse buckets from highest frequency to lowest
        for i in range(len(arr)-1, 0, -1):
            if len(arr[i]) != 0:   # Found the max frequency bucket
                return i * len(arr[i])  # frequency * number of elements

        return 0  # Fallback (shouldn't happen since nums is non-empty)
