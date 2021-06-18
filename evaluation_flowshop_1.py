from FlowShop import FlowShop
from Model import Job, Machine
from draw import *


total_confirm = 0
total_fail = 0
for i in range(1000):

    (jobs, machines) = get_instance(i, has_weight=False, is_flow_shop=True)
    machines = [ Machine(i) for i in range(2)]

    flowshop = FlowShop()
    js_result, js_jobs = flowshop.johnson_rule(jobs, machines)
    opt_result, opt_jobs = flowshop.OPT_Cmax(jobs, machines)


    if (js_result.Cmax == opt_result.Cmax):
        total_confirm += 1
    else:
        total_fail += 1

print("------------------------------------------")
print("Total confirmed  is {}.".format(total_confirm))
print("Total faile  is {}.".format(total_fail))
print("------------------------------------------")
