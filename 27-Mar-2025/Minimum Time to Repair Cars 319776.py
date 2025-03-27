# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def check(time):
            cars_fixed = 0
            for rank in ranks:
                cars_fixed += int((time / rank) ** 0.5)
            return cars_fixed >= cars
        
        left = 1
        right = min(ranks) * cars ** 2
        while right > left:
            mid = (right - left) // 2 + left
            if check(mid):
                right = mid
            else:
                left = mid + 1 
        return right