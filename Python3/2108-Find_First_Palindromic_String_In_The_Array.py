class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # Iterate over all words
        for w in words:

           # Check if the letters equate to their reversed order, then return if true
           if w == w[::-1]:
                return w
        # If not, return an empty string    
        return ""
