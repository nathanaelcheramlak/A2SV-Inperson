# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        products = dict()
        pairs = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                product = nums[i] * nums[j]
                if product not in products:
                    products[product] = 1
                else:
                    pairs += products[product]
                    products[product] += 1

        return (pairs * 8)
