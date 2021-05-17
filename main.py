from OPT import OPT
from PT import PT
from draw import draw, draw_table
from Model import *
from instances import *

print("\n")

machines = [Machine(0), Machine(2), Machine(3)]
jobs = [
    Job(0, 24),
    Job(1, 20),
    Job(2, 4),
    Job(3, 18),
    Job(4, 11),
    Job(5, 24),
    Job(6, 5),
    Job(7, 9),
]

SPT_result = PT(jobs, machines, 'SPT', is_optimize=True, has_weight=False)
print("> SPT")
print("  Cmax : ", SPT_result.Cmax)
print("  Total C : ", SPT_result.total_completion_time)
draw(SPT_result.machines) 

for i in range(1):
    has_weight = False
    (jobs, machines) = get_instance(i, has_weight=has_weight)
    
    LPT_result = PT(jobs, machines, 'LPT', is_optimize=True, has_weight=has_weight)
    SPT_result = PT(jobs, machines, 'SPT', is_optimize=True, has_weight=has_weight)
    OPT_result = OPT(jobs, machines, has_weight=has_weight)

    draw_table(jobs)
    print("> LPT")
    print("  Cmax : ", LPT_result.Cmax)
    print("  Total Completion time : ", LPT_result.total_completion_time)
    draw(LPT_result.machines)

    print("> SPT")
    print("  Cmax : ", SPT_result.Cmax)
    print("  Total Completion time : ", SPT_result.total_completion_time)
    draw(SPT_result.machines) 

    
    print("> OPT")
    print("  Cmax : ", OPT_result.Cmax)
    print("  Total Completion time : ", OPT_result.total_completion_time)
    draw(OPT_result.machines) 

    print()
    print('+++++++++++++++++++++++++++++++++++++++++++++')
    print('+++++++++++++++++++++++++++++++++++++++++++++')
    print()
    # L = LPT_result.Cmax 
    # S = SPT_result.Cmax
    # if S < L:c
    #     draw_table(jobs)
    #     draw(LPT_result.machines, info=True)
    #     # print(LPT_result.Cmax_machine)

    #     draw(SPT_result.machines, info=True) 
    #     # print(SPT_result.Cmax_machine)



# print("\n")
