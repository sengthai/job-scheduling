from Model import Job
from PT import PT
from FlowShop import FlowShop
from draw import draw, draw_table
from OPT import OPT
from instances import get_instance

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