class Solution:


    def rev_recur(self, a: int, b: int, s: List[str]) -> List[str]:
        if a > b:
            return
        s[a], s[b] = s[b], s[a]
        self.rev_recur(a + 1, b - 1, s)
        

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.rev_recur(0, len(s) - 1, s)
            