# This module contains functions and classes for the main algorithm of generating a simulator.
import numpy as np
from backlog import Backlog
from work_item import WorkItem
from release_plan import ReleasePlan
from release_scenario import ReleaseScenario
import numpy_financial as npf

class ReleasePlanSimulator():
    def __init__(self, backlog, H, capacity, L, r, B, N):
        self.backlog = backlog
        self.H = H
        self.capacity = capacity  # list of length H
        self.L = L
        self.r = r
        self.B = B
        self.N = N
        self.effort_simulation = self.generateEffortSimulation()#dictionaries
        self.value_simulation = self.generateValueSimulation()

    #effort and value simulation are dictionaries
    #to access, use effort_simulation[w][number of iteration]
    def generateEffortSimulation(self):
        simulation_dict = {}
        for w in self.backlog.work_items:
            [min, mode, max] = w.effort_est
            simulation_dict[w] = np.random.default_rng().triangular(min, mode, max, self.N)
            
        return simulation_dict

    def generateValueSimulation(self):
        simulation_dict = {}
        for w in self.backlog.work_items:
            [min, mode, max] = w.value_est
            simulation_dict[w] = np.random.default_rng().triangular(min, mode, max, self.N)
            
        return simulation_dict


    # TODO
    def NPV(self, cashflow, rate):
        npv =  npf.npv(rate, cashflow)
        return npv


    def calculate_cashflow(self, s: ReleaseScenario, value_simulation):
        cashflow = []
        #cashflow[0] = sum of value of all work items delivered in period 0
        #cashflow[1] = cashflow[0] + value of workitems delivered in 1
        for release in s:
            sum = 0
            for item in release:
                item_period = s.get_index(release)
                val = value_simulation[item][item_period]
                sum += val
            cashflow.append(sum)
        return cashflow





    # OK
    def punctuality(self, s:ReleaseScenario, p: ReleasePlan):

        nbr_late = 0
        work_items = s.get_work_items()
        for w in work_items:
            if (s.get_delivery_period(w) > p.get_delivery_period(w)):
                nbr_late += 1

        punctuality = (len(work_items) - nbr_late) / len(work_items)

        return punctuality

    # OK
    def value_cost_ratio(self, p: ReleasePlan, n:int):
        ratio_list = []
        for release in p.releases:
            for w in release:
                val = self.value_simulation[w][n]
                cost = self.effort_simulation[w][n]
                ratio = val / cost
                ratio_list.append(ratio)

        return ratio_list

    # OK
    def sort_release(self, a: list, b: list):  # a:the list to be sorted, b: ratio_list
        zipped_list = zip(b, a)
        sorted_zipped_list = sorted(zipped_list)
        sorted_list_a = [element for _, element in sorted_zipped_list]
        return sorted_list_a

    # OK
    def generateWorkSequence(self, p: ReleasePlan):
        ws = []
        for period in p:
            for feature in period:
                ws.append(feature)
        return ws


    # helper function 2
    # n: n-th simulation, p:release plan
    def generateReleaseScenario(self, n: int, p: ReleasePlan):
        # sort each release in the release plan
        ratio = self.value_cost_ratio(p, n)
        for release in p:
            release = self.sort_release(release, ratio)

        # ws is a list of p's work items
        ws = self.generateWorkSequence(p)

        s = ReleaseScenario()#check 

        i = 0
        sumCapacity = self.capacity[i]
        sumEffort = 0
        for w in ws:
            sumEffort = sumEffort + self.effort_simulation[w][n]
            while(sumEffort > sumCapacity):
                i = i + 1
                sumCapacity = sumCapacity + self.capacity[i]
                s.add_release([])
            s.releases[i-1].append(w)

        return s

    # OK
    # main function
    def evaluateReleasePlan(self, p: ReleasePlan):
        sumNPV = 0
        sumPunctuality = 0

        for n in range(self.N):
            s = self.generateReleaseScenario(n, p)
            sumNPV = sumNPV + self.NPV(n, s)
            sumPunctuality = sumPunctuality + self.punctuality(s, p)

        return [(sumNPV/self.N), (sumPunctuality/self.N)]




