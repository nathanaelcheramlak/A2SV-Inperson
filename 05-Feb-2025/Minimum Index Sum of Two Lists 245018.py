# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict_one = { val: index for index, val in enumerate(list1)}

        output = []
        min_idx = len(list1) + len(list2)
        for idx, word in enumerate(list2):
            if word in dict_one:
                idx_sum = idx + dict_one[word]
                if idx_sum == min_idx:
                    output.append(word)
                    min_idx = idx_sum
                elif idx_sum < min_idx:
                    output = [word]
                    min_idx = idx_sum

        return output

