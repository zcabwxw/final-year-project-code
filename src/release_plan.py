from release_sequence import ReleaseSequence


class ReleasePlan(ReleaseSequence):
    def __init__(self, release):
        self.releases = release


