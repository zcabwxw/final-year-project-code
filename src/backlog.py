# backlog contains all the work items.

class Backlog():
    def __init__(self):
        self.work_items = []

    def add_work_items(self, list):
        self.work_items = list

    def __iter__(self):
        for each in self.work_items:
            yield each
