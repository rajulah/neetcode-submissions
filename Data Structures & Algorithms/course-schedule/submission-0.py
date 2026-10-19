class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReqMap = {i : [] for i in range(numCourses)}

        for crs, preReq in prerequisites:
            preReqMap[crs].append(preReq)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            
            if preReqMap[course] == []:
                return True
            visited.add(course)
            for crs in preReqMap[course]:
                if not dfs(crs):
                    return False
            visited.remove(course)
            preReqMap[course] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True