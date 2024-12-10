//Two numbers to sum 2024.12.08
class Solution(object):
    def twoSum(self,nums, target):
        for i in range(len(nums)):
            a = nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] == target - a:
                    return [i,j]
        return ["None"]
