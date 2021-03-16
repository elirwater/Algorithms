class Solution:

    def two_sums_hashmap(self, nums: [int], target) -> [int]:

        hash_map = {}

        idx = 0

        for i in nums:
            hash_map[i] = idx

            if (target - i) in hash_map:
                return [hash_map[target - i], idx]
            idx += 1

s = Solution()
response = Solution.two_sums_hashmap(s, [2, 7, 11, 15], 9)

assert response == [0, 1]
