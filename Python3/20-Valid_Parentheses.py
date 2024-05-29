class Solution(object):
    def isValid(self, s):
        valid = dict(('()', '[]', '{}'))
        stack = []
        for char in s:
            if char in '([{':
                stack.append(char)
            elif len(stack) == 0 or char != valid[stack.pop()]:
                return False
        return len(stack) == 0
