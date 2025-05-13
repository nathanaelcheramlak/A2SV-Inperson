# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        cache = dict()
        def score(start, end):
            if start > end:
                return 0
            if (start + 1, end) not in cache:
                s = nums[start] - score(start + 1, end)
            else:
                s = nums[start] - cache[(start + 1, end)]
            if (start, end - 1) not in cache:
                e = nums[end] - score(start, end - 1)
            else:
                e = nums[end] - cache[(start, end - 1)]

            cache[(start, end)] = max(s, e)
            return max(s, e)
            
        return score(0, len(nums) - 1) >= 0