class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        sorted_nums = sorted(nums)

        left_index = 0
        right_index = len(nums) - 1
        while True:
            left = sorted_nums[left_index]
            right = sorted_nums[right_index]
            if left + right == target:
                break
            if left + right > target:
                right_index -= 1
            else:
                left_index += 1
        
        ans = [nums.index(left), nums.index(right)]
        if ans[0] == ans[1]:
            for i, num in enumerate(nums):
                if num == right and i != ans[0]:
                    ans[1] = i

        return ans
