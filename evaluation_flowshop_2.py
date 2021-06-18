from Model import Job
from PT import PT
from FlowShop import FlowShop
from draw import draw, draw_table
from OPT import OPT
from instances import get_instance


for i in range(1000):
    
    (jobs, machines) = get_instance(seed=i, has_weight=True, is_flow_shop= True,num_of_machines=4, num_of_jobs=4)

    machines = [machines[0]]

    pt_result = PT(jobs, machines, 'SPT', True, has_weight=True)
    opt_result = OPT(jobs, machines, has_weight=True)
    
    print(i)
    print(pt_result.total_completion_time, opt_result.total_completion_time)

    if ((pt_result.total_completion_time/opt_result.total_completion_time) == 1):
        draw_table(jobs)
        draw(pt_result.machines)
        print("Total completion time: {}".format(pt_result.total_completion_time))
        draw(opt_result.machines)
        print("Total completion time: {}".format(opt_result.total_completion_time))
        print("BEST______")
        break

# ╒══════════════╤══════════════╤══════════════╤══════════════╕
# │ j0           │ j1           │ j2           │ j3           │
# ╞══════════════╪══════════════╪══════════════╪══════════════╡
# │ [7, 7, 5, 5] │ [3, 5, 5, 6] │ [3, 4, 4, 5] │ [7, 4, 4, 6] │
# ├──────────────┼──────────────┼──────────────┼──────────────┤
# │ 7            │ 16           │ 15           │ 20           │
# ╘══════════════╧══════════════╧══════════════╧══════════════╛
(jobs, machines) = get_instance(seed=3, has_weight=True, is_flow_shop= True,num_of_machines=4, num_of_jobs=4)

draw_table(jobs)

print("\n | ---------- WSPT ---------- | \n")
pt_result = PT(jobs, [machines[0]], 'SPT', True, has_weight=True)
draw(pt_result.machines)
print("Total completion time: {}".format(pt_result.total_completion_time))       
print("Cmax : {}".format(pt_result.Cmax_machine.get_Cmax()))

print("\n | ---------- OPT ---------- | \n")
opt_result = OPT(jobs, [machines[0]], has_weight=True)
draw(opt_result.machines)
print("Total completion time: {}".format(opt_result.total_completion_time))
print("Cmax : {}".format(opt_result.Cmax_machine.get_Cmax()))

print("\n | ---------- FlowShop WSPT ---------- | \n")
pt_fs_result, temp_jobs = FlowShop().PT(jobs, machines, 'SPT', has_weight=True)
draw(pt_fs_result.machines)
print("Total completion time: {}".format(pt_fs_result.total_completion_time))
print("Cmax : {}".format(pt_fs_result.Cmax))

print("\n | ---------- FlowShop OPT ---------- | \n")
fs_result, temp_jobs = FlowShop().OPT(jobs, machines)
draw(fs_result.machines)
print("Total completion time: {}".format(fs_result.total_completion_time))
print("Cmax : {}".format(fs_result.Cmax))
