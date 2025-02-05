# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # Bruteforce
        good_count = 0
        char = Counter(chars)

        for word in words:
            map = Counter(word)
            for key, value in map.items():
                freq = char.get(key, 0)
                if map[key] > freq:
                    map.clear()
                    break
            print(map)
            good_count += sum(value for key, value in map.items())
        
        return good_count

            
