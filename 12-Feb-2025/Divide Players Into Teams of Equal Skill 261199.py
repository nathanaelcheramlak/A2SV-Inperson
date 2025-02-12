# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill) - 1
        chemistry = 0
        summ = skill[left] + skill[right]
        while right > left:
            if skill[left] + skill[right] != summ:
                return -1
            else:
                chemistry += (skill[left] * skill[right])
            left += 1
            right -= 1
        
        return chemistry