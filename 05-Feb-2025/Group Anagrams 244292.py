# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = dict()

        for word in strs:
            sorted_word = str(sorted(word))
            # map[sorted_word] = map.get(sorted_word, []).append(word)

            if sorted_word not in map:
                map[sorted_word] = [word]
            else:
                map[sorted_word].append(word)
        
        return list(map.values())