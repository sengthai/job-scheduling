

from itertools import permutations
from typing_extensions import final
from Model import Job, Machine, Result
from PT import PT
from instances import get_instance
from copy import deepcopy
import numpy as np
from draw import draw, draw_Cmax, draw_series_job


class FlowShop:

    def PT(self, jobs, machines, rule: str, has_weight=False):
        all_jobs = deepcopy(jobs)

        # check the rule if it is LPT or SPT
        is_reverse = (rule == 'LPT')
        
        if has_weight:
            all_jobs.sort(key=lambda x: np.sum(x.weight_ratio), reverse=(not is_reverse))
        else:
            all_jobs.sort(reverse=is_reverse)

        pt_result = self.gantt_chart(all_jobs, deepcopy(machines))
    
        return (pt_result, all_jobs)
    
    def OPT_Cmax(self, jobs, machines):

        all_jobs = deepcopy(jobs)
        
        # combination of list of all jobs
        all  = list(permutations(all_jobs))
        final_result  = ()

        for al in all:
            temp_jobs = deepcopy(al)
            temp_machine = deepcopy(machines)
            result = self.gantt_chart(temp_jobs, temp_machine)

            if final_result is ():
                final_result = (result, temp_jobs)
                continue

            # compare the makespan
            if result.Cmax < final_result[0].Cmax:
                final_result = (result, temp_jobs)

            del temp_jobs
            del temp_machine

        return final_result

    def OPT(self, jobs, machines):

        all_jobs = deepcopy(jobs)
        
        # combination of list of all jobs
        all  = list(permutations(all_jobs))
        final_result  = ()

        for al in all:
            temp_jobs = deepcopy(al)
            temp_machine = deepcopy(machines)
            result = self.gantt_chart(temp_jobs, temp_machine)

            if final_result is ():
                final_result = (result, temp_jobs)
                continue
            
            if result.total_completion_time < final_result[0].total_completion_time:
                final_result = (result, temp_jobs)

            del temp_jobs
            del temp_machine

        return final_result
    
    def johnson_rule(self, jobs, machines):
        assert len(machines) == 2

        process_times = [ i.process_time for i in jobs ]
        
        all_jobs = deepcopy(jobs)

        Ma = []
        Mb = []

        while(True):

            shortest_arg = np.argwhere(process_times == np.min(process_times))[0]
            
            job = all_jobs.pop(shortest_arg[0])

            if shortest_arg[1] == 0: 
                Ma.append(job)
            else:
                Mb.insert(0, job)

            del process_times[shortest_arg[0]]

            if len(all_jobs) == 0:
                break

        list_job_order = Ma + Mb
        result = self.gantt_chart(list_job_order, deepcopy(machines))
        return (result, list_job_order)

    def gantt_chart(self, jobs, machines):
        for job in jobs:
            for idx, process_time in enumerate(job.process_time):
                machines[idx].jobs.append(Job(job.id, process_time, job.weight))
        Cmax = 0
        Cmax_machine = None
        for pt_index in range(len(jobs)):

            for ma_index, machine in enumerate(machines):

                IN_a = 0 if ma_index == 0 else machines[ma_index-1].jobs[pt_index].OUT
                IN_b = 0 if pt_index == 0 else machine.jobs[pt_index-1].OUT

                IN = max(IN_a, IN_b)
                OUT = machine.jobs[pt_index].process_time + IN

                ma1 = 0 if ma_index == 0 else machines[ma_index-1].jobs[pt_index].OUT
                ma2 = 0 if pt_index == 0 else machine.jobs[pt_index-1].OUT

                idle = max(0, (ma1-ma2) )
                machine.jobs[pt_index].IN = IN
                machine.jobs[pt_index].OUT = OUT
                machine.jobs[pt_index].idle = idle

                if OUT >= Cmax:
                    Cmax = OUT
                    Cmax_machine = machine
        


        # total_completion_time = np.sum([ m.get_total_completion_time_2() for m in machines])
        total_completion_time = machines[-1].get_total_completion_time_2()
        
        return Result(machines, Cmax_machine, total_completion_time, Cmax)
    


