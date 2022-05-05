
from platform import release
import pandas as pd
from release_plan import ReleasePlan
from backlog import Backlog
from work_item import WorkItem
from simulator import ReleasePlanSimulator
#install openpyxl
import seaborn as sns
import matplotlib.pyplot as plt


#read file
file = pd.ExcelFile('./src/Council-Backlog-Raw.xlsx')
df_parameters = pd.read_excel(file,sheet_name='Planning Parameters')
df_backlog = pd.read_excel(file,sheet_name='Backlog & dependencies')
df_effort = pd.read_excel(file, sheet_name='Effort Estimates')
df_value = pd.read_excel(file, sheet_name='Value Estimates')

#read parameters
planning_horizon = df_parameters['Planning Horizon'][0]
capacity_one = df_parameters['Capacity (man-hours)'][0]
capacity = planning_horizon * [int(capacity_one)]

investment_horizon = df_parameters['Investment Horizon'][0]
discount_rate = df_parameters['Discount rate'][0]
budget = df_parameters['Budget (£1,000)'][0]

#backlog work items
backlog = Backlog()
name_list = []
for name in df_backlog['Work Items']:
    name_list.append(name)

work_item_list = []
max_iter = len(df_effort['Work Items'])
i = 0
for i in range(max_iter):
    label = df_effort['Work Items'][i]
    effort_low = df_effort['Lower Quartile'][i]
    effort_med = df_effort['Median'][i]
    effort_high = df_effort['Upper Quartile'][i]
    effort_est = [effort_low, effort_med, effort_high]

    value_low = df_value['Lower Quartile'][i]
    value_med = df_value['Median'][i]
    value_high = df_value['Upper Quartile'][i]
    value_est = [value_low, value_med, value_high]

    if label in name_list:
        if (effort_est != [0,0,0] and value_est != [0,0,0]):
            w = WorkItem(label)
            w.add_effort_est(effort_low, effort_med, effort_high)
            w.add_value_est(value_low, value_med, value_high)
            work_item_list.append(w)

    i += 1

backlog.add_work_items(work_item_list)


#Release Plan 1
df_plan = pd.read_excel('./src/Council-Backlog-Plan.xlsx')
release_plan = ReleasePlan()
period_list = ['Period 0', 'Period 1', 'Period 2']
for i in period_list:
    item_list = []
    for item in df_plan[i]:
        for w in backlog.work_items:
            if (item == w.label):
                item_list.append(w)
    release_plan.add_release(item_list)

#Release Plan 2
df_plan2 = pd.read_excel('./src/Council-Backlog-Plan2.xlsx')
release_plan2 = ReleasePlan()
period_list2 = ['Period 0', 'Period 1', 'Period 2']
for i in period_list2:
    item_list = []
    for item in df_plan2[i]:
        for w in backlog.work_items:
            if (item == w.label):
                item_list.append(w)
    release_plan2.add_release(item_list)

#Release Plan 3
df_plan3 = pd.read_excel('./src/Council-Backlog-Plan3.xlsx')
release_plan3 = ReleasePlan()
period_list3 = ['Period 0', 'Period 1', 'Period 2']
for i in period_list3:
    item_list = []
    for item in df_plan3[i]:
        for w in backlog.work_items:
            if (item == w.label):
                item_list.append(w)
    release_plan3.add_release(item_list)




sim = ReleasePlanSimulator(backlog, planning_horizon, capacity, investment_horizon, discount_rate, budget, 100000)
e = sim.evaluateReleasePlan(release_plan)
print(e)
npv_dis = sim.npv_distribution(release_plan)

e2 = sim.evaluateReleasePlan(release_plan2)
print(e2)
npv_dis2 = sim.npv_distribution(release_plan2)

e3 = sim.evaluateReleasePlan(release_plan3)
print(e3)
npv_dis3 = sim.npv_distribution(release_plan3)


sns.displot(npv_dis, kde=True)
plt.title('NPV distribution over 100000 iterations: Release Plan A')
plt.xlabel('NPV')
plt.ylabel('Count')
plt.show()

sns.displot(npv_dis2, kde=True)
plt.title('NPV distribution over 100000 iterations: Release Plan B')
plt.xlabel('NPV')
plt.ylabel('Count')
plt.show()

'''
sns.displot(npv_dis3, kde=True)
plt.title('NPV distribution over 100000 iterations: Release Plan C')
plt.xlabel('NPV')
plt.ylabel('Count')
plt.show()
'''