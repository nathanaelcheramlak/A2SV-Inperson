# Problem: Water Bottles - https://leetcode.com/problems/water-bottles/description

class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        total = numBottles
        remainder = 0
        while numBottles >= numExchange:
            total += numBottles // numExchange
            remainder = numBottles % numExchange
            numBottles = (numBottles // numExchange) + remainder
        return total 