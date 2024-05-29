class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # Search through haystack to see if it contains the needle string
        index = haystack.find(needle)

        # Account for if the needle isn't present by returning -1
        if index == -1:
            return -1

        # If the needle is present, return its index
        else:
            return int(index)
