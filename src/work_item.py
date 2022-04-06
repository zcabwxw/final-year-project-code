

class WorkItem():
    def __init__(self, label: str):
        self.effort_est = []
        self.value_est = []
        self.label = label


    # add effort/value estimation
    def add_effort_est(self, min: int, mode: int, max: int):
        self.effort_est = [min, mode, max]

    def add_value_est(self, min: int, mode: int, max: int):
        self.value_est = [min, mode, max]



