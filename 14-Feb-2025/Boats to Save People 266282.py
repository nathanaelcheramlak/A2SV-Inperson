# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        left = 0
        right = len(people) - 1

        while right > left:
            curr = people[right] + people[left]
            if curr <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            count += 1
        if right == left:
            count += 1
        return count