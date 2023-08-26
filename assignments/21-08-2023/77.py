class Solution:
    def helper(self, n, start, processed, answer, k):
        if k == 0:
            answer.append(processed.copy())
            return

        if k > n - start + 1:
            return

        processed.append(start)
        self.helper(n, start + 1, processed, answer, k - 1)
        processed.pop()  
        self.helper(n, start + 1, processed, answer, k)

    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        self.helper(n, 1, [], answer, k)
        return answer