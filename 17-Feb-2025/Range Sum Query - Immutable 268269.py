# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.fullSum()

    def fullSum(self):
        lst = [0]
        for n in self.nums:
            sum = n + lst[-1]
            lst.append(sum)
        self.sum = lst

    def sumRange(self, left: int, right: int) -> int:
        return self.sum[right+1] - self.sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)