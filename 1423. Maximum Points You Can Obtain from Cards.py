# 1423. Maximum Points You Can Obtain from Cards
class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        max_sum=0
        for i in range(k+1):
            curr=0
            for l in range(k+1):
                curr+=cardPoints[l]
            for r in range(k-i):
                curr+=cardPoints[n-1-r]
            max_sum=max(curr,max_sum)
        return max_sum