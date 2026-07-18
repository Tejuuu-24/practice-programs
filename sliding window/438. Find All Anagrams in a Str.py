# LeetCode 438. Find All Anagrams in a String.
class Solution(object):
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []

        p_freq = {}
        window_freq = {}
        res = []

        # Frequency of p
        for ch in p:
            p_freq[ch] = p_freq.get(ch, 0) + 1

        # First window
        for i in range(len(p)):
            window_freq[s[i]] = window_freq.get(s[i], 0) + 1

        if window_freq == p_freq:
            res.append(0)

        # Sliding window
        for i in range(len(p), len(s)):
            left = s[i - len(p)]

            window_freq[left] -= 1
            if window_freq[left] == 0:
                del window_freq[left]

            window_freq[s[i]] = window_freq.get(s[i], 0) + 1

            if window_freq == p_freq:
                res.append(i - len(p) + 1)

        return res