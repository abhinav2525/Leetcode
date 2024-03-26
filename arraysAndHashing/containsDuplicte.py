class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        noDuplicate = set() # create a set to store unique elements

        # iterate through the list of numbers
        for num in nums:
            if num in noDuplicate:
                return True
            noDuplicate.add(num)

        return False