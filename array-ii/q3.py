"""
Question:
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
"""


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        # 数字がすべて揃っている場合の配列をsetで用意
        complete_nums = set(range(1, n + 1))

        # numsの数字をsetから削除していく
        for num in nums:
            if num in complete_nums:
                complete_nums.remove(num)

        return list(complete_nums)
