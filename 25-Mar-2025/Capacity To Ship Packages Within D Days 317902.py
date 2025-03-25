# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity):
            total, ships = 0, 1
            for weight in weights:
                if total + weight > capacity:
                    ships += 1
                    total = 0
                total += weight

            return ships <= days
        
        left = max(weights)
        right = sum(weights)
        while right > left:
            mid = (left + right) // 2
            if canShip(mid):
                right = mid 
            else:
                left = mid + 1
        
        return right