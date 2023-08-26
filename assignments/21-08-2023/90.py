class Solution:
    def helper(self, nums, index, subset, answer):
        if index >= len(nums):
            answer.append(subset.copy())
            return

        subset.append(nums[index])
        self.helper(nums, index + 1, subset, answer)
        subset.pop()
        while index + 1 < len(nums) and nums[index] == nums[index + 1]:
            index += 1
        self.helper(nums, index + 1, subset, answer)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums = sorted(nums)
        self.helper(nums, 0, [], answer)
        return answer