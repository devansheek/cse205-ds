class Solution:
    def helper(self, answer, open, closed, n, processed):
        if len(processed) == 2 * n:
            answer.append(processed)
            return

        if open < n:
            self.helper(answer, open + 1, closed, n, processed + '(')

        if closed < open:
            self.helper(answer, open, closed + 1, n, processed + ')')


    def generateParenthesis(self, n: int) -> List[str]:
       answer = []
       self.helper(answer, 0, 0, n, "")
       return answer