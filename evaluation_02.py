from numpy.lib.function_base import append, average
from OPT import OPT
from PT import PT
from draw import draw, draw_table
from Model import *
from instances import *

print("\n")


SPTs = []
OPTs = []

for i in range(1000):

    has_weight = True
    (jobs, machines) = get_instance(i, has_weight=has_weight)
    
    SPT_result = PT(jobs, machines, 'SPT', is_optimize=True, has_weight=has_weight)
    OPT_result = OPT(jobs, machines, has_weight=has_weight)
   
    SPTs.append(SPT_result)
    OPTs.append(OPT_result)
    print(i)
    draw_table(jobs)


    print("> SPT")
    draw(SPT_result.machines) 

    print("> OPT")
    draw(OPT_result.machines)


   

spt_avg_ratio = sum([ i.total_completion_time for i in SPTs]) / len(SPTs)
opt_avg_ratio = sum([ i.total_completion_time for i in OPTs]) / len(OPTs)

# print("\n")
print('+++++++++++++++ The Ratio (average) +++++++++++++++++++')
print("The Total Completion time SPT and OPT:")
print("     - WSPT: {}".format(spt_avg_ratio))
print("     - OPT: {}".format(opt_avg_ratio))
print("     -> WSPT/OPT = {}".format(str(spt_avg_ratio/opt_avg_ratio)))
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print()
