class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # Remove extra whitespaces
        stripped = s.strip()

        # Create a map containing the length of the final word
        words = list(map(len, stripped.split()))

        # Create a variable containing the length of the final word
        final = words[-1]

        # Account for if there are no words after removing whitespaces by returning zero
        if words == 0:
            return 0

        # Otherwise, return the length of the last element in the list of words
        else:
            return int(str(final))
