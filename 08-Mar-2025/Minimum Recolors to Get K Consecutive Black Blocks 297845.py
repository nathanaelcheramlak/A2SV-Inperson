# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        window = Counter(blocks[:k])
        answer = window['W']

        for left in range(len(blocks) - k):
            window[blocks[left]] -= 1
            window[blocks[left + k]] += 1
            answer = min(answer, window['W'])
        
        return answer