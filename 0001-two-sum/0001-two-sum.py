class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, n in enumerate(nums):
            difff = target - n

            if difff in hashmap:
                return [hashmap[difff], i]
            else:
                hashmap[n] = i
        return