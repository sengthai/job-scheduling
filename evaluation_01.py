from numpy.lib.function_base import append, average
from OPT import OPT
from PT import PT
from draw import draw, draw_table
from Model import *
from instances import *

print("\n")


LPTs = []
SPTs = []
OPTs = []

for i in range(1000):

    has_weight = False
    (jobs, machines) = get_instance(i, has_weight=has_weight)
    
    LPT_result = PT(jobs, machines, 'LPT', is_optimize=True, has_weight=has_weight)
    SPT_result = PT(jobs, machines, 'SPT', is_optimize=True, has_weight=has_weight)
    OPT_result = OPT(jobs, machines, has_weight=has_weight)
   
    SPTs.append(SPT_result)
    LPTs.append(LPT_result)
    OPTs.append(OPT_result)
   
    draw_table(jobs)
    print("> LPT")
    draw(LPT_result.machines)

    print("> SPT")
    draw(SPT_result.machines) 

    print("> OPT")
    draw(OPT_result.machines)

    print('+++++++++++++++ Compare +++++++++++++++++++')
    print("Makespan:")
    print("     - LPT: {}".format(LPT_result.Cmax))
    print("     - SPT: {}".format(SPT_result.Cmax))
    print("     - OPT: {}".format(OPT_result.Cmax))
    print("Total Completion Time")
    print("     - LPT: {}".format(LPT_result.total_completion_time))
    print("     - SPT: {}".format(SPT_result.total_completion_time))
    print("     - OPT: {}".format(OPT_result.total_completion_time))
    print('+++++++++++++++++++++++++++++++++++++++++++++')
    print()
    print()


   
    print()


lpt_avg_cmax = sum([ i.Cmax for i in LPTs]) / len(LPTs)
spt_avg_cmax = sum([ i.Cmax for i in SPTs]) / len(SPTs)
opt_avg_cmax = sum([ i.Cmax for i in OPTs]) / len(OPTs)

lpt_avg_total = sum([ i.total_completion_time for i in LPTs]) / len(LPTs)
spt_avg_total = sum([ i.total_completion_time for i in SPTs]) / len(SPTs)
opt_avg_total = sum([ i.total_completion_time for i in OPTs]) / len(OPTs)


# print("\n")
print('+++++++++++++++ THE ALL COMPARE (average) +++++++++++++++++++')
print("Makespan:")
print("     - LPT: {}".format(lpt_avg_cmax))
print("     - SPT: {}".format(spt_avg_cmax))
print("     - OPT: {}".format(opt_avg_cmax))
print("Total Completion Time")
print("     - LPT: {}".format(lpt_avg_total))
print("     - SPT: {}".format(spt_avg_total))
print("     - OPT: {}".format(opt_avg_total))
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print()
