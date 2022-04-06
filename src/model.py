# Work item
import numpy as np

class WorkItem():
    def __init__(self, label: str, index: int):
        self.effort_est = []
        self.value_est = []
        self.label = label


    # add effort/value estimation
    def add_effort_est(self, min: int, mode: int, max: int):
        self.effort_est = [min, mode, max]

    def add_value_est(self, min: int, mode: int, max: int):
        self.value_est = [min, mode, max]


# Product Backlog
class Backlog():
    def __init__(self, N, H, capacity, L, r, B):
        self.work_items = []
        self.N = N
        self.H = H
        self.capacity = capacity
        self.L = L
        self.r = r
        self.B = B
        self.effort_simulation = []
        self.value_simulation = []



    # add workitems
    def add_work_items(self, workItem: WorkItem):
        self.work_items.append(workItem)

    def __iter__(self):
        for each in self.work_items:
            yield each


    def generate_effort_simulation(self):
        for w in self.work_items:
            [min, mode, max] = w.effort_est
            self.effort_simulation.append(np.random.default_rng().triangular(min, mode, max, self.N))

        self.effort_simulation = np.array(self.effort_simulation)
        return self.effort_simulation

    def generate_value_simulation(self):
        for w in self.work_items:
            [min, mode, max] = w.value_est
            self.value_simulation.append(np.random.default_rng().triangular(min, mode, max, self.N))

        self.value_simulation = np.array(self.value_simulation)
        return self.value_simulation





# Release plan
class ReleasePlan():
    def __init__(self):
        self.releases = []

    def add_release(self, release: list):
        self.releases.append(release)

    def get_release(self, id: int):
        return self.releases[id]

    def get_index(self, release: list):
        pos = -1
        for i in range(len(self.releases)):
            if (self.releases[i] == release):
                pos = i
        return pos

    def get_length(self):
        count = 0
        for release in self.releases:
            length = len(release)
            count += length
        return count

    def __iter__(self):
        for each in self.releases:
            yield each

