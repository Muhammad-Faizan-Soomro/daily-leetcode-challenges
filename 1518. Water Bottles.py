# Problem: 1518. Water Bottles
# Task:
# - You have `numBottles` full bottles of water.
# - After drinking a bottle, it becomes empty.
# - You can exchange `numExchange` empty bottles for 1 full bottle.
# - Return the maximum number of bottles you can drink.
#
# Example:
#   numBottles = 9, numExchange = 3
#   Step 1: Drink 9 → 9 empty
#   Step 2: Exchange 9 empty → 3 full, drink them (total = 12), left with 3 empty
#   Step 3: Exchange 3 empty → 1 full, drink it (total = 13), left with 1 empty
#   Answer = 13
#
# Approach (Simulation):
# 1. Start with `numBottles` and set total `drink = numBottles`.
# 2. While total empty bottles >= numExchange:
#       - Exchange them to get new full bottles.
#       - Drink these new bottles and add to `drink`.
#       - Update remaining bottles after exchange.
# 3. Return the total drinks.
#
# Time Complexity: O(n / numExchange)   -> each loop reduces empty bottles
# Space Complexity: O(1)                -> constant extra space
#
# Note: The loop continues until not enough empty bottles remain for an exchange.

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        totalBottles = numBottles
        drink = totalBottles
    
        while totalBottles >= numExchange:
            # After drinking, all are empty
            emptyBottles = totalBottles

            # Exchange empty bottles for new full ones
            exchangedBottles = emptyBottles // numExchange
            drink += exchangedBottles

            # Leftover bottles after exchange
            remainingBottles = emptyBottles % numExchange

            # New total bottles to consider
            totalBottles = exchangedBottles + remainingBottles
        
        return drink
