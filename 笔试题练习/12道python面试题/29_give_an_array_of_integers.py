class Solution(object):
    def twosum(self,nums,target):
        """
        给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。你可以假设每个输入只对应一种答
        案，且同样的元素不能被重复利用。示例:给定nums = [2,7,11,15],target=9 因为 nums[0]+nums[1] =
        2+7 =9,所以返回[0,1]
        :param nums: list[int]
        :param target: int
        :return: list[int]
        """
        d = {}
        size = 0
        while size < len(nums):
            if target - nums[size] in d:
                if d[target-nums[size]] < size:
                    return [d[target-nums[size]],size]
                else:
                    d[nums[size]] = size
                size = size + 1


class Solution2(object):
    def twosum(self,nums,target):
        for i in range(len(nums)):
            num = target - nums[i]
            if num in nums[i+1:]:
                return [i,nums.index(num,i+1)]

if __name__ == '__main__':
    solution = Solution2()
    list = [2,11,7,15]
    target = 9
    nums = solution.twosum(list, target)
    print(nums)
