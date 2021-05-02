class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hash_map = defaultdict(set)
        for course, prereq in prerequisites:
            hash_map[course].add(prereq)
        wont_create_cycle = set()
        def has_cycle(course, visited_path):
            nonlocal wont_create_cycle, hash_map
            if course in visited_path:
                return True
            if course in wont_create_cycle:
                return False
            if course not in hash_map:
                return False
            visited_path.add(course)
            for prereq in hash_map[course]:
                if has_cycle(prereq, visited_path):
                    return True
                else:
                    wont_create_cycle.add(prereq)
            visited_path.remove(course)
            return False
        for course in range(numCourses):
            if has_cycle(course, set()):
                return False
            else:
                wont_create_cycle.add(course)
        return True