class Solution:
    def arePermutations(self, s1, s2):
        c = [0] * 26
        for i in range(len(s1)):
            c[ord(s1[i]) - ord('a')] += 1
            c[ord(s2[i]) - ord('a')] -= 1
        # print(s1,s2,c)
        for i in c:
            if i != 0:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        left = 0
        right = len(s1)
        while right <= len(s2):
            if self.arePermutations(s1, s2[left:right]):
                return True
            left += 1
            right += 1
        return False

