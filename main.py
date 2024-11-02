class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rnums = []
        check = False
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    rnums.append([i, j])
                    check = True
                    break
            if check:
                break

        print(rnums[0])


nums = list(map(int, input().strip('[]').split(',')))
target = int(input())
solution = Solution()
solution.twoSum(nums, target)

