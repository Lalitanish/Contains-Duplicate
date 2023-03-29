class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        nums.sort()
        hashset = set()
        for number in nums:
            if number in hashset:
                return True
            hashset.add(number)
        return False















