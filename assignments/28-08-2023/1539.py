class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        total = []
        for i in range (arr[-1] + 1 + k):
            if i not in arr:
                total.append(i)
        return total[k]
        