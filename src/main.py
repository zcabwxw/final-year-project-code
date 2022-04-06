from platform import release
import simulator
from simulator import ReleasePlanSimulator
from work_item import WorkItem
from backlog import Backlog
from release_plan import ReleasePlan
from release_scenario import ReleaseScenario
from release_sequence import ReleaseSequence


# assign values to a work item.
w1 = WorkItem(label='wi1')
w1.add_effort_est(10,20,30)
w1.add_value_est(20,40,60)

w2 = WorkItem(label='wi2')
w2.add_effort_est(10,20,30)
w2.add_value_est(20,40,60)

w3 = WorkItem(label='wi3')
w3.add_effort_est(10,20,30)
w3.add_value_est(20,40,60)


# add work items to a backlog
backlog = Backlog()
backlog.work_items = [w1,w2,w3]


sim = simulator.ReleasePlanSimulator(backlog,N=10,H=2, capacity=[10,20,20,20,20], L=2, r=0.1, B=0)

releasePlan = ReleasePlan([[w1],[w2],[w3]])

releaseScenario = sim.generateReleaseScenario(1, releasePlan)

#e = sim.evaluateReleasePlan(releasePlan)

cashflow = sim.calculate_cashflow(releaseScenario, sim.value_simulation)
npv = sim.NPV(cashflow, sim.r)
print(npv)