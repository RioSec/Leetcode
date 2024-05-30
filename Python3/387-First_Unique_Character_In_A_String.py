class Solution:
    def firstUniqChar(self, s: str) -> int:

        # Create a default dictionary that is automatically initialized
        count = defaultdict(int) # char -> count

        # For each character that repeats, add one to its value
        for c in s:
            count[c] += 1

        # Find the first index of a unique letter and return it using an enumeration
        for i, c in enumerate(s):
            if count[c] == 1:
                return i

        # If therse isn't an applicable letter, return -1 
        return -1
