class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = {}
        for n in nums:
            if res.get(n):
                res[n] += 1
            else:
                res[n] = 1
        for key, val in res.iteritems():
            if val == 1:
                return key
