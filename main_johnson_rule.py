from FlowShop import FlowShop
from numpy.lib.function_base import append, average
from OPT import OPT
from PT import PT
from draw import *
from Model import *
from instances import *

jobs = [
    Job(0, [15,6]),
    Job(1, [32,19]),
    Job(2, [8,13]),
    Job(3, [27,20]),
    Job(4, [11,14]),
    Job(5, [16,7]),
]

machines = [ Machine(i) for i in range(2)]

flowshop = FlowShop()
draw_table(jobs)
print("\n | ---------- Johnson rule ---------- | \n")
js_result, js_jobs = flowshop.johnson_rule(jobs, machines)
draw_series_job(js_jobs)
draw(js_result.machines, True)
draw_Cmax(js_result.Cmax_machine.id, js_result.Cmax)

print("\n | --------  Full Enumeration ------- | \n")
opt_result, opt_jobs = flowshop.OPT_Cmax(jobs, machines)
draw_series_job(opt_jobs)
draw(opt_result.machines, True)
draw_Cmax(opt_result.Cmax_machine.id, opt_result.Cmax)

print("\n | ------------  SPT Rule ---------- | \n")
pt_result, pt_jobs  = flowshop.PT(jobs, machines, 'SPT')
draw_series_job(pt_jobs)
draw(pt_result.machines, True)
draw_Cmax(pt_result.Cmax_machine.id, pt_result.Cmax)