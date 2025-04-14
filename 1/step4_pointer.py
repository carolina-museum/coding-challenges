class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        sorted_nums = sorted(nums)

        left_index = 0
        right_index = len(nums) - 1
        while True:
            left_num = sorted_nums[left_index]
            right_num = sorted_nums[right_index]
            if left_num + right_num == target:
                break
            if left_num + right_num > target:
                right_index -= 1
                continue
            left_index += 1
        
        ans = [nums.index(left_num), nums.index(right_num)]
        if ans[0] == ans[1]:
            ans[1] = nums.index(right_num, ans[0]+1)
        
        return ans
