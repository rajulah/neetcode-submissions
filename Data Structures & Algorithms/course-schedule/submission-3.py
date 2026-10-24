class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            prereqMap[course].append(prereq)
        
        visited = set()
        def dfs(course):
            if prereqMap[course] == []:
                return True
            if course in visited:
                return False
            visited.add(course)
            for prereq in prereqMap[course]:
                if not dfs(prereq):
                    return False
            prereqMap[course] = []
            visited.remove(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True