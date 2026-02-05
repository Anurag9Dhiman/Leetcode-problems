# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

#SOlution using backtracking

class Solution:
    def permute(self, nums:list[int]) -> list[list[int]]:
        res = []
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i]=True
                    path.append(nums[i])
                    backtrack(path)
                    path.pop()
                    used[i] = False

        backtrack([])
        return res
        