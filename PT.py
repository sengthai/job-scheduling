from copy import copy, deepcopy

from Model import Result

import numpy as np


# This method is used to calcuate the processing time algorithm 
# (LPT, SPT, WSPT, LPT)
def PT(jobs, machines, rule: str, is_optimize=True, has_weight=False):

    sort_jobs: list = deepcopy(jobs)

    # check if the job's process is list
    if jobs and type(sort_jobs[-1].process_time) is list:
        for job in sort_jobs:
            job.process_time = sum(job.process_time)

    machines = deepcopy(machines)

    # check the rule if it is LPT or SPT
    is_reverse = (rule == 'LPT')

    # check it has weight
    if has_weight:
        # sort by the weight ratio ( weight/process_time )
        sort_jobs.sort(key=lambda x: x.weight_ratio, reverse= (not is_reverse))
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
