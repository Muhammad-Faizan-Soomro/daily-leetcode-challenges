# Problem: 812. Largest Triangle Area
# Task:
# - Given a list of points on a 2D plane, return the largest area of a triangle formed by any three points.
#
# Example:
#   points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
#   Possible triangles → compute areas
#   Maximum area = 2.0 (triangle formed by (0,2), (2,0), (0,0))
#
# Approach:
# 1. Iterate over all possible triplets of points (i, j, k).
# 2. Use the shoelace formula to calculate the area:
#    Area = 0.5 * | x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2) |
# 3. Keep track of the maximum area found.
# 4. Return the maximum area after checking all triplets.
#
# Time Complexity: O(n^3)  -> three nested loops over n points
# Space Complexity: O(1)   -> only a few variables, no extra storage
#
# Note: Constraints allow n ≤ 50, so O(n^3) is efficient enough.

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        area = 0.0
        n = len(points)

        # Step 1: Iterate through all triplets
        for i in range(0, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]

                    # Step 2: Compute area using shoelace formula
                    A = abs((x1 * (y2 - y3)) +
                            (x2 * (y3 - y1)) +
                            (x3 * (y1 - y2))) / 2

                    # Step 3: Update max area
                    if A > area:
                        area = A

        # Step 4: Return maximum area
        return area
