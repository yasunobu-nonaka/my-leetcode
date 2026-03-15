class Solution:
    def smallerNumbersThanCurrent(self, nums):
        count = [0] * 101

        for n in nums:
            count[n] += 1

        for i in range(1, 101):
            count[i] += count[i - 1]

        ans = []
        for n in nums:
            if n == 0:
                ans.append(0)
            else:
                ans.append(count[n - 1])

        return ans
