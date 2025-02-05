# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        total_even = sum(num for num in nums if num % 2 == 0)
        ans = list()

        for val, idx in queries:
            temp = nums[idx] + val
            print(temp)
            if temp % 2 == 0:
                if nums[idx] % 2 == 0: # If it was even before the addition
                    total_even += (temp - nums[idx])
                else:
                    total_even += temp
            else:
                if nums[idx] % 2 == 0:
                    total_even -= nums[idx]
                    
            nums[idx] = temp
            ans.append(total_even)
        
        return ans