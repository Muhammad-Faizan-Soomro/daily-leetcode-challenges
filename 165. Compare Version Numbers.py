# Problem: 165. Compare Version Numbers
# Task:
# - Given two version strings (e.g., "1.01", "1.0.0", "1.0.2"),
#   compare them part by part.
# - Return:
#       1  if version1 > version2
#      -1  if version1 < version2
#       0  if both are equal
#
# Example:
#   version1 = "1.01", version2 = "1.001"
#   After removing leading zeros → [1, 1] vs [1, 1] → result = 0
#
#   version1 = "1.0", version2 = "1.0.0"
#   Normalized → [1, 0, 0] vs [1, 0, 0] → result = 0
#
#   version1 = "1.0.2", version2 = "1.0.10"
#   Normalized → [1, 0, 2] vs [1, 0, 10]
#   Compare → 2 < 10 → result = -1
#
# Approach:
# 1. Split both versions by "." into lists of revision numbers.
# 2. Pad the shorter list with zeros so both lists are equal length.
# 3. Remove leading zeros from each revision and convert to int.
# 4. Compare revisions one by one:
#       - If v1 > v2 → return 1
#       - If v1 < v2 → return -1
# 5. If all parts equal → return 0
#
# Time Complexity: O(n * m)
#   - n = max number of parts in version1 or version2
#   - m = max length of any revision string (for leading zero removal)
#   - Splitting, padding, cleaning, comparing → O(n * m)
#
# Space Complexity: O(n)
#   - Lists to hold normalized version parts
#   - No extra complex data structures
#
# Note: Can be optimized further by skipping explicit zero-stripping 
#       since int("001") already becomes 1 in Python.

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Step 1: Split versions into parts
        converted_01 = version1.split(".")
        converted_02 = version2.split(".")

        # Step 2: Pad both lists to same length
        max_len = max(len(converted_01), len(converted_02))
        converted_01 += ['0'] * (max_len - len(converted_01))
        converted_02 += ['0'] * (max_len - len(converted_02))

        # Step 3: Normalize parts of version1 (remove leading zeros, convert to int)
        for i in range(len(converted_01)):
            if converted_01[i].startswith('0') and len(converted_01[i]) != 1:
                j = 0
                while converted_01[i][j] == '0':
                    j += 1
                    if j == len(converted_01[i]):  # Handle "000" → "0"
                        j -= 1
                        break
                converted_01[i] = converted_01[i][j:]
            converted_01[i] = int(converted_01[i])

        # Step 4: Normalize parts of version2 (same process as version1)
        for i in range(len(converted_02)):
            if converted_02[i].startswith('0') and len(converted_02[i]) != 1:
                j = 0
                while converted_02[i][j] == '0':
                    j += 1
                    if j == len(converted_02[i]):  # Handle "000" → "0"
                        j -= 1
                        break
                converted_02[i] = converted_02[i][j:]
            converted_02[i] = int(converted_02[i])

        # Step 5: Compare revisions one by one
        for i in range(len(converted_01)):
            if converted_01[i] > converted_02[i]:
                return 1
            elif converted_01[i] < converted_02[i]:
                return -1

        # Step 6: Versions are equal
        return 0
