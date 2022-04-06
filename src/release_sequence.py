from model import WorkItem


class ReleaseSequence():
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


    def get_delivery_period(self, w:WorkItem):
        for release in self.releases:
            for item in release:
                if w == item:
                    return self.get_index(release)

    def get_work_items(self):
        list = []
        for release in self.releases:
            for item in release:
                list.append(item)
        return list

    def __iter__(self):
        for each in self.releases:
            yield each

