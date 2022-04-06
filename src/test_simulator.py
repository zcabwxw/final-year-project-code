from platform import release
import unittest
from simulator import ReleasePlanSimulator
from work_item import WorkItem
from backlog import Backlog
from release_plan import ReleasePlan
from release_scenario import ReleaseScenario
from release_sequence import ReleaseSequence


class TestReleasePlanSimulator(unittest.TestCase):
    def __init__(self):
        self.w1 = WorkItem(label='wi1')
        self.w1.add_effort_est(10,20,30)
        self.w1.add_value_est(20,40,60)
        self.w2 = WorkItem(label='wi2')
        self.w2.add_effort_est(10,20,30)
        self.w2.add_value_est(20,40,60)
        self.w3 = WorkItem(label='wi3')
        self.w3.add_effort_est(10,20,30)
        self.w3.add_value_est(20,40,60)

        self.release_plan1 = ReleasePlan([[self.w1],[self.w2],[self.w3]])
        self.release_plan2 = ReleasePlan([self.w1],[],[self.w2])
        
        self.release_scenario1 = ReleasePlan([self.w1], [self.w2], [self.w3])
        self.release_scenario2 = ReleasePlan([self.w1], [self.w2], [])

   




if __name__ == '__main__':
    unittest.main()

