class Solution:
    def removeVowels(self, S):
        return "".join(c for c in S if c not in "aeiou")

        
