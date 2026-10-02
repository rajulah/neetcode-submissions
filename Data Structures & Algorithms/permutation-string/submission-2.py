class Solution:
    def compareHashmaps(self, map1, map2):
        if len(map1) != len(map2):
            return False
        for key, value in map1.items():
            if key not in map2:
                return False
            if map1[key] != map2[key]:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Counts = {}
        for s in s1:
            s1Counts[s] = s1Counts.get(s, 0) + 1
        
        charMap = {}

        left = 0
        for right in range(len(s2)):
            charMap[s2[right]] = charMap.get(s2[right], 0) + 1

            if right - left + 1 > len(s1):
                charMap[s2[left]] -= 1

                if charMap[s2[left]] == 0:
                    del charMap[s2[left]]
                left += 1
            if right - left + 1 == len(s1):
                if self.compareHashmaps(s1Counts, charMap):
                    return True
        return False

            