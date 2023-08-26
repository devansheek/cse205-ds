class Solution:
    def helper(self, candidates, target, i, total, res, answer):
        if total == target:
            answer.append(res.copy())
            return

        if i >= len(candidates) or total > target:
            return

        res.append(candidates[i])
        self.helper(candidates, target, i + 1, total + candidates[i], res, answer)
        res.pop()

        while i + 1 < len(candidates) and candidates[i] == candidates[i+1]: #checks if next element is duplicate
                i = i + 1
        self.helper(candidates, target, i + 1, total, res, answer)


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates = sorted(candidates)
        self.helper(candidates, target, 0, 0, [], answer)
        return answer