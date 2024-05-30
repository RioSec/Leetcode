class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Clean the string so it only contains alphanumeric characters
        s= re.sub(r'[^a-zA-Z0-9]', '', s)

        # Make all the characters in the string lowercase
        s=s.lower()

        # Write the reversed version of the string to a variable
        rev_s=s[::-1]

        # If the reversed version equals the original, return true. Else return false. 
        if s==rev_s:
            return True
        else:
            return False
