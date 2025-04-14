class Solution:
    @staticmethod
    def target_exists(nums_sorted, start_i, end_i, value_to_look_for):

        while True:
            if value_to_look_for in (nums_sorted[start_i], nums_sorted[end_i]):
                return True
            
            if end_i - start_i <= 1:  # 終了条件
                return False

            mid_index = (start_i + end_i)//2

            if nums_sorted[mid_index] == value_to_look_for:
                return True
            elif nums_sorted[mid_index] < value_to_look_for:
                start_i = mid_index
            else:
                end_i = mid_index

        return False # return something just in case we didn't return anything at this point


    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        nums_sorted = sorted(nums)

        for i in range(len(nums)):
            focus_value = nums_sorted[i]
            value_to_look_for = target - nums_sorted[i]

            if Solution.target_exists(nums_sorted, i, len(nums)-1, value_to_look_for):
                break

        first_i = nums.index(focus_value)  # 2つの要素が同じ値を持つ場合でも、２種類のindexを返したい
        for i in range(len(nums)):
            if i == first_i:
                continue
            if nums[i] == value_to_look_for:
                second_i = i
                return [first_i, second_i]
