class Solution:
    def smallerNumbersThanCurrent(self, nums):
        # numsをソート
        sorted_nums = sorted(nums)
        rank = {}

        # 各数字が最初に現れたインデックスを取り出す => ある数字より小さい数字の数
        for i, v in enumerate(sorted_nums):
            if v not in rank:
                rank[v] = i

        return [rank[v] for v in nums]


if __name__ == "__main__":
    nums = [8, 1, 2, 2, 3]
    solution = Solution()
    result = solution.smallerNumbersThanCurrent(nums)
    print(result)
