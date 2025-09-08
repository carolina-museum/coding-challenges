class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        #binary-search
        left = 0
        right = len(nums) - 1

        while left <= right:
            pos = (left + right) // 2
            if nums[pos] == target:
                return pos
            elif target < nums[pos]:
                right = pos - 1
            else:
                left = pos + 1
        
        return left