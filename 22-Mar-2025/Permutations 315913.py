# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(i, path, seen):
            nonlocal ans
            if len(path) == len(nums):
                ans.append(path[:])
                return
            
            for i in range(len(nums)):
                if nums[i] in seen:
                    continue
                path.append(nums[i])
                seen.add(nums[i])
                backtrack(i + 1, path, seen)
                seen.discard(path.pop())
        
        backtrack(0, [], set())
        return ans