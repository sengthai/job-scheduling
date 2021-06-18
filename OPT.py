from numpy.lib.function_base import insert
from Model import Machine, Result
from copy import deepcopy, copy
from itertools import permutations 

# Full enumration algorihtm (OPT, OPT with weight)
def OPT(jobs, machines, has_weight=False):

    temp_jobs: list = deepcopy(jobs)

    if jobs and type(temp_jobs[-1].process_time) is list:
        for job in temp_jobs:
            job.process_time = sum(job.process_time)

    machines: list = deepcopy(machines)

    # combination of all possible jobs
    all  = list(permutations(temp_jobs))

    # store the best optimal solution
    insts = []
    
    # find all possible solutions
    for ls in all:
        jbs = deepcopy(list(ls))
        ms: list = deepcopy(machines)
        while jbs:
            for i in ms:
                if jbs:
                    j = jbs.pop(0)
                    i.jobs.append(deepcopy(j))
                else: break

        # find the bigest cmax in machinces
        cmax_machine = ms[0]
        for m in ms:
            m0 = cmax_machine.get_Cmax()
            m1 = m.get_Cmax()
            if m1 > m0:
                cmax_machine = m
        
        if insts:
            # apply algorithm if it has weight
            if has_weight:
                width_ratio_inst = sum([ deepcopy(m).get_total_completion_time() for m in insts[0]])
                width_ratio_ms = sum([ deepcopy(m).get_total_completion_time() for m in ms])
                if width_ratio_ms < width_ratio_inst :
                    insts = [ms[:], cmax_machine]
            else:
                # compare the Cmax 
                if insts[1].get_Cmax() > cmax_machine.get_Cmax():
                    insts = [ms[:], cmax_machine] 
        else:
            insts = [ms[:], cmax_machine] 

    # calcuate the total completion time
    total_completion_time = sum([ m.get_total_completion_time()for m in insts[0]])
    result = Result(insts[0], insts[1], total_completion_time)
    return result
