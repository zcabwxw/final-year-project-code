import unittest
from model import WorkItem, Backlog, ReleasePlan


class TestWorkItem(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestWorkItem, self).__init__(*args, **kwargs)
        self.effort_est = []
        self.value_est = []

    pass


class TestBacklog(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestBacklog, self).__init__(*args, **kwargs)
    pass


class TestReleasePlan(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestReleasePlan, self).__init__(*args, **kwargs)

    def test_get_release(self):
        releasePlan = ReleasePlan()
        releasePlan.add_release([1,2,3])
        releasePlan.add_release([4,5,6])
        releasePlan.add_release([7,8,9])
        result = ReleasePlan.get_release(releasePlan,0)
        self.assertEqual(result, [1,2,3])

    def test_get_index(self):
        releasePlan = ReleasePlan()
        releasePlan.add_release([1,2,3])
        releasePlan.add_release([4,5,6])
        releasePlan.add_release([7,8,9])
        result = ReleasePlan.get_index(releasePlan, [4,5,6])
        self.assertEqual(result, 1)

    def test_get_length(self):
        releasePlan = ReleasePlan()
        releasePlan.add_release([1,2,3])
        releasePlan.add_release([4,5,6])
        releasePlan.add_release([7,8,9])
        result = ReleasePlan.get_length(releasePlan)
        self.assertEqual(result, 9)


if __name__ == '__main__':
    unittest.main()
