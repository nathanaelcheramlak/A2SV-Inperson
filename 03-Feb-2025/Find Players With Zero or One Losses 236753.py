# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        my_dict = dict()

        for win, loss in matches:
            my_dict[loss] = my_dict.get(loss, 0) + 1
            my_dict[win] = my_dict.get(win, 0)
        
        ans = [[], []]
        for key, value in my_dict.items():
            if value == 1:
                ans[1].append(key)
            if value == 0:
                ans[0].append(key)
        
        return [sorted(ans[0]), sorted(ans[1])]
