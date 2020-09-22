import sys
import heapq


class PracticableProjects(object):
    def __init__(self):
        self._queue = []

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, item))

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def visit(self):
        return self._queue[0][-1]

    def qsize(self):
        return len(self._queue)

    def empty(self):
        return True if not self._queue else False


class ImpracticableProjects(object):
    def __init__(self):
        self._queue = []

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, item))

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def visit(self):
        return self._queue[0][-1]

    def qsize(self):
        return len(self._queue)

    def empty(self):
        return True if not self._queue else False


class Project(object):
    def __init__(self, cost, revenue):
        self.cost = cost
        self.revenue = revenue


def project_selection(c, k):
    practicable_projects = PracticableProjects()
    impraticable_projects = ImpracticableProjects()
    for ci in cr:
        cur_project = Project(ci[0], ci[1])
        if ci[0] <= c:
            practicable_projects.push(cur_project, cur_project.revenue - cur_project.cost)
        else:
            impraticable_projects.push(cur_project, cur_project.cost)
    for i in range(k):
        if practicable_projects.qsize() == 0:
            return "impossible"
        new_project = practicable_projects.pop()
        c += new_project.revenue - new_project.cost
        while (not impraticable_projects.empty() and c > impraticable_projects.visit().cost):
            new_practicable_project = impraticable_projects.pop()
            practicable_projects.push(new_practicable_project,
                                      new_practicable_project.revenue - new_practicable_project.cost)
    return c


a = [int(s) for s in sys.stdin.readline().split()]
cr = [[int(t) for t in s.split(':')] for s in sys.stdin.readline().split()]
for _ in range(a[1]):
    b = [int(s) for s in sys.stdin.readline().split()]
    c, k = b[0], b[1]
    print(project_selection(c, k))
