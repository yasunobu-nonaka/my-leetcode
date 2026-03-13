class Solution:
    # def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    def smallerNumbersThanCurrent(self, nums):
        ans = []
        n = len(nums)

        # 数字を一つずつより小さい数字が何個あるか調べる
        for i in range(n):
            count = 0
            j = 0
            while j < n:
                # 見た数が小さければcount + 1
                if j != i and nums[j] < nums[i]:
                    count += 1
                j += 1
            ans.append(count)

        return ans


if __name__ == "__main__":
    cases = [[8, 1, 2, 2, 3], [6, 5, 4, 8], [7, 7, 7, 7]]
    solution = Solution()
    for case in cases:
        result = solution.smallerNumbersThanCurrent(case)
        print(result)
