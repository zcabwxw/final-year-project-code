from platform import release
import unittest
from simulator import ReleasePlanSimulator
from work_item import WorkItem
from backlog import Backlog
from release_plan import ReleasePlan
from release_scenario import ReleaseScenario
from release_sequence import ReleaseSequence


class TestReleasePlanSimulator(unittest.TestCase):
    def setUp(self):
        self.w1 = WorkItem(label='wi1')
        self.w1.add_effort_est(10,20,30)
        self.w1.add_value_est(20,40,60)
        self.w2 = WorkItem(label='wi2')
        self.w2.add_effort_est(10,20,30)
        self.w2.add_value_est(20,40,60)
        self.w3 = WorkItem(label='wi3')
        self.w3.add_effort_est(10,20,30)
        self.w3.add_value_est(20,40,60)

        self.release_plan1 = ReleaseSequence([[self.w1],[self.w2],[self.w3]])
        self.release_plan2 = ReleaseSequence([[self.w1],[],[self.w2]])
        
        self.release_scenario1 = ReleaseSequence([[self.w1], [self.w2], [self.w3]])
        self.release_scenario2 = ReleaseSequence([[], [self.w1], []])
        self.release_scenario3 = ReleaseSequence([[self.w1], [],[]])

        self.backlog = Backlog()
        self.backlog.add_work_items([self.w1, self.w2, self.w3])
        self.simulator = ReleasePlanSimulator(self.backlog, N=100,H=5, capacity=[20,20,20,20,20], L=2, r=0.1, B=0)


    def test_NPV(self):
        cashflow = [100,100,100]
        rate = 0.1
        npv = self.simulator.NPV(cashflow, rate)
        real_value = 100.0/1.0 + 100.0/(1.1) + 100.0/(1.1**2)
        self.assertEqual(npv, real_value)


    def test_punctuality(self):
        p = self.release_plan1
        s1 = self.release_scenario1
        punc = self.simulator.punctuality(s1, p)
        self.assertEqual(punc, 1)

    def test_punctuality2(self):
        p = self.release_plan1
        s2 = self.release_scenario2
        punc = self.simulator.punctuality(s2,p)
        self.assertEqual(punc, 0)

    def test_punctuality3(self):
        p = self.release_plan1
        s3 = self.release_scenario3
        punc = self.simulator.punctuality(s3, p)
        self.assertEqual(punc, 1/3)

    def test_generate_release_scenario(self):
        n = 9
        p = self.release_plan1
        s = self.simulator.generateReleaseScenario(n,p)
        #print(s.releases)

    def test_generate_work_sequence(self):
        p = self.release_plan1
        ws = self.simulator.generateWorkSequence(p)
        self.assertEqual(len(ws), 3)
    
    def test_value_cost_ratio(self):
        p = self.release_plan1
        n = 10
        ratio = self.simulator.value_cost_ratio(p, n)
        pass

    


if __name__ == '__main__':
    unittest.main()

