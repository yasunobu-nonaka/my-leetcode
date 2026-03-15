class Solution:
    # def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    def smallerNumbersThanCurrent(self, nums):
        n = len(nums)
        ans = [0] * n
        # 数字を一つずつ見てそれより小さい他の数字が何個あるか調べる
        for i in range(n):
            for j in range(i + 1, n):
                # 自分のが大きければ自身の位置のカウントを+1
                if nums[j] < nums[i]:
                    ans[i] = ans[i] + 1
                # 相手のが大きければ相手の位置のカウントを+1
                elif nums[j] > nums[i]:
                    ans[j] = ans[j] + 1

        return ans


if __name__ == "__main__":
    cases = [[8, 1, 2, 2, 3], [6, 5, 4, 8], [7, 7, 7, 7]]
    solution = Solution()
    for case in cases:
        result = solution.smallerNumbersThanCurrent(case)
        print(result)
