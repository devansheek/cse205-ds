class Solution:
    def recur(self, nums, output, index, answer):
    #base
        if index >= len(nums):
            answer.append(output.copy())
            return

    #exclude
        self.recur(nums, output, index + 1, answer)

    #include
        element = nums[index]
        output.append(element)
        self.recur(nums, output, index + 1, answer)
        output.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        output = []
        index = 0

        self.recur(nums, output, index, answer)
        return answer