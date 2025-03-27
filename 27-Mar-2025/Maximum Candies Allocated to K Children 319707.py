# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def possible(person):
            count = 0
            for candy in candies:
                count += candy // person
            return count >= k

        left = 0
        right = sum(candies) // k
        while right > left:
            mid = (right - left) // 2 + left + 1
            if possible(mid):
                left = mid 
            else:
                right = mid - 1
        
        return left