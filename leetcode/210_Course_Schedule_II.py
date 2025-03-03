from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dependencies = {}
        for course, prerequisite in prerequisites:
            if course not in dependencies:
                dependencies[course] = []
            dependencies[course].append(prerequisite)

        already_taken = set()
        loop = set()
        result = []

        def dfs(course):
            if course in already_taken:
                return True
            if course in loop:
                return False
            loop.add(course)
            if course in dependencies:
                for j in dependencies[course]:
                    if not dfs(j):
                        return False
            loop.remove(course)
            result.append(course)
            already_taken.add(course)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return result
