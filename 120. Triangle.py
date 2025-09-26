# Problem: 120. Triangle
# Task:
# - Given a triangle array (list of lists), return the minimum path sum 
#   from top to bottom.
# - At each step, you may move to the adjacent numbers in the row below.
#
# Example:
#   Input:
#   [
#        [2],
#       [3,4],
#      [6,5,7],
#     [4,1,8,3]
#   ]
#   Output: 11
#   Explanation: 2 → 3 → 5 → 1 = 11
#
# Approach (Bottom-Up DP):
# - Start from the second last row and move upward.
# - At each cell, replace its value with:
#       value + min(path_sum_below_left, path_sum_below_right)
# - The top element will eventually hold the minimum total path sum.
#
# Submission #1:
# - Modifies the original triangle (in-place).
# - At each step, updates triangle[row][col] directly.
#
# Time Complexity: O(n^2)  -> we visit each cell once.
# Space Complexity: O(1)   -> in-place DP, no extra storage.
#
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle) - 2  # start from 2nd last row
        tri = triangle

        # Bottom-up DP
        for row in range(n, -1, -1):
            for col in range(0, row + 1):
                tri[row][col] = tri[row][col] + min(tri[row+1][col], tri[row+1][col+1])
                
        return tri[0][0]


# Submission #2:
# - Uses a 1D array `tri` initialized as the last row of the triangle.
# - Instead of modifying the full 2D structure, compresses space.
# - Updates only the relevant path sums row by row (rolling DP array).
#
# Time Complexity: O(n^2)  -> still processes all elements.
# Space Complexity: O(n)   -> uses extra array for bottom row.
#
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle) - 2  # start from 2nd last row
        tri = triangle[len(triangle) - 1]  # bottom row

        # Bottom-up DP with 1D compression
        for row in range(n, -1, -1):
            for col in range(0, row + 1):
                tri[col] = triangle[row][col] + min(tri[col], tri[col+1])
                
        return tri[0]
