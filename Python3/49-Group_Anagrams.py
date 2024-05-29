# Import default dictionary structure
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize the default dictionary
        anagram_map = defaultdict(list)

        # Create a list to store the result
        result = []

        # For each letter per string, sort them alphabeticall, then create a key 
        for s in strs:
            sorted_s = tuple(sorted(s))
 
            # Write the value letters to the the key
            anagram_map[sorted_s].append(s)

        # For each value present in values, append the value to the result list. Then return it. 
        for value in anagram_map.values():
            result.append(value)

        return result
