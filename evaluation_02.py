from numpy.lib.function_base import append, average
from OPT import OPT
from PT import PT
from draw import draw, draw_table
from Model import *
from instances import *


SPTs = []
OPTs = []

for i in range(10):

    has_weight = True
    (jobs, machines) = get_instance(i, has_weight=has_weight, is_flow_shop=False)
    
    SPT_result = PT(jobs, machines, 'SPT', is_optimize=True, has_weight=has_weight)
    OPT_result = OPT(jobs, machines, has_weight=has_weight)
   
    SPTs.append(SPT_result)
    OPTs.append(OPT_result)
    print(i)




    if SPT_result.total_completion_time <= OPT_result.total_completion_time:
        draw_table(jobs)
        print("> WSPT")
        draw(SPT_result.machines) 

        print("> OPT")
        draw(OPT_result.machines)
        print("")



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
