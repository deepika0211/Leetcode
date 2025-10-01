class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
            new = numBottles
            empty= numBottles
            while empty >= numExchange:
                newBottles = empty//numExchange
                new += newBottles
                empty = newBottles + (empty%numExchange)
            return new

