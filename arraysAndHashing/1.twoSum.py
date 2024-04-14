class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: # type: ignore
        prevNumMap = {} # key is the number, value is the index

        for i,n in enumerate(nums): # enumerate returns index and value
            difference = target - n # find the difference between the target and the current number
            if difference in prevNumMap:
                return [prevNumMap[difference],i] # return the index of the difference and the current indexS
            prevNumMap[n] = i # store the number and its index in the map
