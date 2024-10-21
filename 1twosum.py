class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution = []
        for i in range(len(nums)):
            num1 = nums[i]
            for j in range(i + 1, len(nums), 1):
                num2 = nums[j]
                if num1+num2 == target:
                    solution.append(i)
                    solution.append(j)
                    return solution
            
