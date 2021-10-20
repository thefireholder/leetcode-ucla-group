# Backtracking, recursion
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.generate(n, n, "", result)
        return result
    
    def generate(self, left, right, temp, result):
        if left == 0 and right == 0:
            result.append(temp)
            return
        if left > 0:
            self.generate(left-1, right, temp+'(', result)
        if right > left:
            self.generate(left, right-1, temp + ')', result)

'''
Runtime: 24 ms, faster than 99.28% of Python3 online submissions for Generate Parentheses.
Memory Usage: 14.8 MB, less than 11.81% of Python3 online submissions for Generate Parentheses.
'''