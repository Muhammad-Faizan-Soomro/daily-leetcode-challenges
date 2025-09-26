# Problem: 611. Valid Triangle Number
# Task:
# - Given an array of integers (side lengths), count the number of triplets (i, j, k) 
#   that can form a valid triangle.
# - A triangle is valid if: a + b > c for any sides a, b, c.
#
# Example:
#   Input: nums = [2, 2, 3, 4]
#   Output: 3
#   Explanation:
#       Valid triangles: (2,3,4), (2,3,4), (2,2,3)
#
# Approach:
# - Sort the array to ensure nums[i] ≤ nums[j] ≤ nums[k].
# - Fix the largest side (nums[k]), and then check how many (i, j) pairs 
#   satisfy nums[i] + nums[j] > nums[k].
#
# ----------------------------------------------------------------------
# Submission #1: Two-Pointer Approach
# - Fix nums[k] as the largest side.
# - Use two pointers (i, j) to find valid pairs:
#       - If nums[i] + nums[j] > nums[k], 
#             then all pairs from i...j-1 with nums[j] also form valid triangles.
#             → count += j - i
#             → move j left (j -= 1)
#       - Else, move i right (i += 1).
#
# Time Complexity: O(n^2)   -> nested loop with 2-pointer traversal
# Space Complexity: O(1)    -> constant extra space
#
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
            
        nums.sort()
        count = 0

        # Fix largest side as nums[k]
        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += j - i  # all pairs between i and j are valid
                    j -= 1
                else:
                    i += 1
                    
        return count


# ----------------------------------------------------------------------
# Submission #2: Binary Search Approach
# - Fix nums[i] and nums[j] as the first two sides.
# - Use binary search to find the largest index k such that:
#       nums[i] + nums[j] > nums[k]
# - All elements between (j+1) and k are valid third sides.
# - Accumulate count += (k - j).
#
# Time Complexity: O(n^2 log n)  -> nested loops with binary search
# Space Complexity: O(1)
#
class Solution:
    def BinarySearch(self, arr, L, R, target):
        k = -1
        # Find rightmost index < target
        while L <= R:
            mid = L + (R - L) // 2
            if arr[mid] < target:
                k = mid
                L = mid + 1
            else:
                R = mid - 1
        return k

    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
            
        nums.sort()
        count = 0

        # Fix first two sides nums[i], nums[j]
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                tar = nums[i] + nums[j]
                k = self.BinarySearch(nums, j + 1, n - 1, tar)
                if k != -1:
                    count += k - j
                    
        return count
