def course_schedule(numCourses, prerequisites):
    # this is a graph problem, so we need a dfs approach
    # and an adjList, a visit set to detect cycle
    adjList = { i: [] for i in range(numCourses)}

    for pre, crs in prerequisites:
        adjList[pre].append(crs)

    visit = set()

    def dfs(crs):
        # if crs is in visit set, we detected a cycle
        if crs in visit:
            return False
        # if value of current crs is [] -> we can reach this course
        if adjList[crs] = []:
            return True

        # else, we add crs to visitSet for consideration
        visit.add(crs)

        # loop through the values of current course with dfs
        for pre in adjList[crs]:
            if not dfs(pre): return False

        visit.remove(crs)
        adjList[crs] = []

        return True

    for crs in range(numCourses):
        if not dfs(crs): return False

    return True
