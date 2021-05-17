from copy import copy, deepcopy
from typing import Optional

from numpy.lib.utils import info
from draw import draw, draw_table
from Model import Machine, Result
from instances import get_instance
from itertools import groupby


# This method is used to calcuate the processing time algorithm 
# (LPT, SPT, WSPT, LPT)
def PT(jobs, machines, rule: str, is_optimize=True, has_weight=False):

    sort_jobs: list = deepcopy(jobs)
    machines = deepcopy(machines)

    # check the rule if it is LPT or SPT
    is_reverse = (rule == 'LPT')

    # check it has weight
    if has_weight:
        # sort by the weight ratio ( weight/process_time )
        sort_jobs.sort(key=lambda x: x.weight_ratio, reverse=is_reverse)
    else:
        sort_jobs.sort(reverse=is_reverse)

    if is_optimize:
        # select the next machine for jobs when it has less Cmax
        while sort_jobs:
            m = min(machines, key = lambda x: x.get_Cmax())
            j = sort_jobs.pop(0)
            m.jobs.append(copy(j))
    else:
        # assign the job to the machine by order
        while sort_jobs:
            for m in (machines):
                if sort_jobs:
                    j = sort_jobs.pop(0)
                    m.jobs.append(copy(j))
                else: break  

    cmax_machine = machines[0]
    total_completion_time = 0

    # find the largest Cmax of machincess
    for m in machines:
        m0 = cmax_machine.get_Cmax()
        m1 = m.get_Cmax()
        if m1 > m0:
            cmax_machine = m
        total_completion_time += m.get_total_completion_time()

    result = Result(machines, cmax_machine, total_completion_time)

    return result




def select_machine(machines):
    # check all machinces has the same jobs
    
    number_of_jobs = [ len(i.jobs) for i in machines]
    
    # if all m has no jobs
    if len(machines[0].jobs) == 0:
        return machines[0]

    # check if all machines have the same jobs
    if all_equal(number_of_jobs):
        j = max(machines, key = lambda x: x.get_total_completion_time())
        return j
        
    return min(machines, key = lambda x: x.get_total_completion_time())

    
    

def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)
