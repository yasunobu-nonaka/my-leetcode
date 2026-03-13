class Solution:
    # def findErrorNums(self, nums: List[int]) -> List[int]:
    def findErrorNums(self, nums):
        # 本来想定される配列
        expected = list(range(1, len(nums) + 1))

        # 重複している数字と欠けている数字
        duplicated = None
        missing = None

        # numsの数字を１つずつexpectedから取り除く
        for num in nums:
            if num in expected:
                expected.remove(num)
            else:
                # 存在しない場合それが重複しているもの
                duplicated = num

        # 残るということはnumsに存在しない数字なので欠けている数字
        if len(expected) == 1:
            missing = expected[0]

        return [duplicated, missing]


if __name__ == "__main__":
    cases = [[1, 2, 2, 4], [1, 1], [1, 2, 3, 4, 5, 6, 1], [1, 2, 3, 2, 5], [3, 2, 2]]
    solution = Solution()
    for case in cases:
        print(solution.findErrorNums(case))
