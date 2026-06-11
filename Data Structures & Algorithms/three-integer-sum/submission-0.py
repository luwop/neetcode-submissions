class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        -4 -1 -1 0 1 2 
        """

        nums.sort()
        res = set()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 

            j = i + 1
            k = len(nums) - 1

            while j < k:
                target = nums[i] + nums[j] + nums[k]

                if target > 0:
                    k -= 1
                elif target < 0:
                    j += 1
                else:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1

        return [ list(trip) for trip in res]