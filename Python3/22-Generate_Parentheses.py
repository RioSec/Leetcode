class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for i in range(n + 1)]
        dp[0].append('')

        # iterate over all f(0) ... f(n) parenthesis pair targets
        for i in range(n + 1):

           # iterate over all solutions generated thus far --> f(0) ... f(i)
            for j in range(i):
                to_be_added = []

                # iterate over all solutions for f(j)
                for x in dp[j]:

                   # iterate over all solutions for f(n - j)
                    for y in dp[i - j - 1]:

                       # insert solution for f(j) between parens
                        # --> and add all solutions for f(n - j) to back
                        to_be_added.append('(' + x + ')' + y)

                dp[i] += to_be_added

        return dp[n]
