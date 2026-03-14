class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        current_length = 0
        max_length = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current_length += 1
            else:
                current_length = 0

            if current_length > max_length:
                max_length = current_length

        return max_length
