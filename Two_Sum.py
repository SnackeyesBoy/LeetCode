//Two numbers to sum 2024.12.08
class Solution(object):
    print("Input:")
    nums = input("nums = ").split()
    nums = [int(i) for i in nums]
    target = input("target = ")
    print(nums)
    print(target)

    def twoSum(self,nums, target):
        for i in range(len(nums)):
            a = nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] == target - a:
                    return [i,j]
        return ["None"]
                
solution = Solution()
output = solution.twoSum()
print("Output:",output)          
