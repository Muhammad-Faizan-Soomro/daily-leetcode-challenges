# Problem: 1039. Minimum Score Triangulation of Polygon
# Task:
# - Given a convex polygon with vertices labeled 0 to n-1 (in order),
#   and each vertex has a value, find the minimum possible score of triangulation.
# - Score of a triangle = product of its three vertices' values.
# - Goal: partition polygon into triangles with minimum total score.
#
# Example:
#   values = [1, 2, 3]
#   Only one triangle possible -> score = 1 * 2 * 3 = 6
#
#   values = [3, 7, 4, 5]
#   Possible triangulations:
#     (3,7,4) + (3,4,5) = 3*7*4 + 3*4*5 = 84 + 60 = 144
#     (3,7,5) + (7,4,5) = 3*7*5 + 7*4*5 = 105 + 140 = 245
#   Minimum = 144
#
# Approach (DP + Memoization):
# 1. Use recursion with memoization (top-down DP).
# 2. Define solve(i, j) = minimum score to triangulate polygon from vertex i to j.
# 3. Base case: if (j - i < 2), no triangle can be formed -> return 0.
# 4. Transition:
#    - Choose a middle vertex k (i < k < j).
#    - Form triangle (i, k, j) and recursively solve subproblems:
#      solve(i, k) + values[i]*values[k]*values[j] + solve(k, j).
# 5. Take the minimum over all possible k.
#
# Time Complexity: O(n^3)   -> n^2 states, each considering O(n) partitions
# Space Complexity: O(n^2)  -> recursion + memoization cache
#
# Note: Classic polygon triangulation problem solved with interval DP.

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)

        @lru_cache(None)
        def solve(i, j):
            if j - i < 2:
                return 0  # Base case: less than 3 vertices

            result = float('inf')
            # Try all possible middle points
            for k in range(i + 1, j):
                weight = solve(i, k) + values[i] * values[k] * values[j] + solve(k, j)
                result = min(result, weight)

            return result

        return solve(0, n - 1)
