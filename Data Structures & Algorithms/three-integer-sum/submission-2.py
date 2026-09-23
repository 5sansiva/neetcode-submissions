class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1 
            while l < r:
                tempSum = nums[i] + nums[l] + nums[r]
                temparray = [nums[i], nums[l], nums[r]]
                if tempSum == 0 and temparray not in output:
                    output.append(temparray)
                elif tempSum > 0:
                    r -= 1
                else:
                    l += 1
                
        return output       