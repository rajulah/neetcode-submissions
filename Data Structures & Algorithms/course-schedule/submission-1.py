class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # given array of prerequisites
        # prerequisite [i] = [a,b]
        prereqMap = {i : [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            prereqMap[course].append(prereq)
        currVisited = set()
        def dfs(crs):
            if prereqMap[crs] == []:
                return True
            
            if crs in currVisited:
                return False
            currVisited.add(crs)
            for req in prereqMap[crs]:
                if not dfs(req):
                    return False
            currVisited.remove(crs)
            prereqMap[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True