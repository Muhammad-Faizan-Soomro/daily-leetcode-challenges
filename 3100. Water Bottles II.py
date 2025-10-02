# Problem: 3100. Water Bottles II
# Task:
# - You have `numBottles` full bottles of water.
# - After drinking a bottle, it becomes empty.
# - You can exchange `numExchange` empty bottles for 1 full bottle.
# - However, after each exchange, the number of bottles needed for the next exchange increases by 1.
# - Return the maximum number of bottles you can drink.
#
# Example:
#   numBottles = 13, numExchange = 6
#   Step 1: Drink 13 → 13 empty
#   Step 2: Exchange 6 → 1 full, drink it (total = 14), left with 8 empty, next exchange needs 7
#   Step 3: Exchange 7 → 1 full, drink it (total = 15), left with 2 empty, next exchange needs 8
#   No more exchanges possible → Answer = 15
#
# Approach (Simulation):
# 1. Start with `numBottles` and set `drunkBottles = numBottles`.
# 2. While enough empty bottles remain for exchange:
#       - Use `numExchange` empty bottles to get 1 full bottle.
#       - Increase `drunkBottles` count.
#       - Increase `numExchange` by 1 for the next round.
#       - Update empty bottles accordingly.
# 3. Return total `drunkBottles`.
#
# Time Complexity: O(drunkBottles)  -> each loop accounts for one extra drink
# Space Complexity: O(1)            -> only counters are used
#
# Note: The problem differs from 1518 (Water Bottles I) because the exchange rate increases after each exchange.

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        emptyBottles = numBottles
        drunkBottles = numBottles

        while emptyBottles >= numExchange:
            # Use empty bottles for 1 exchange
            emptyBottles -= numExchange
            numExchange += 1   # Next exchange requires more bottles
            drunkBottles += 1  # Drink the new bottle
            emptyBottles += 1  # That new bottle becomes empty after drinking
                
        return drunkBottles
