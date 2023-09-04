class Solution:
    def sum_of_elements(self, nums):
        if len(nums) == 1:
            return nums
        res = []
        for i in range (1, len(nums)):
            addition = nums[i] + nums[i - 1]
            if addition > 9:
                res.append(addition % 10)
            else:
                res.append(addition)
        return self.sum_of_elements(res)

    def triangularSum(self, nums: List[int]) -> int:
        answer = self.sum_of_elements(nums)
        return answer[0]
            