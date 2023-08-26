class Solution:
    def helper(self, candidates, target, i, total, res, answer):
        if total == target:
            answer.append(res.copy())
            return

        if i >= len(candidates) or total > target:
            return

        res.append(candidates[i])
        self.helper(candidates, target, i, total + candidates[i], res, answer)
        res.pop()
        self.helper(candidates, target, i + 1, total, res, answer)


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        self.helper(candidates, target, 0, 0, [], answer)
        return answer