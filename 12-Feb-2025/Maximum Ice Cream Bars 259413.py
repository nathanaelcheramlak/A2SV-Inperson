# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        ice_cream = 0
        max_element = min(coins, max(costs))
        bucket = [0] * (max_element + 1)

        for cost in costs:
            if cost <= max_element:
                bucket[cost] += 1
        
        target = 0
        for idx, val in enumerate(bucket):
            while val > 0:
                coins -= idx
                ice_cream += 1
                val -= 1
                if coins < 0:
                    print('me')
                    return ice_cream - 1

        if ice_cream == 0:
            return 0
        return len(costs)