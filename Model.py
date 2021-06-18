import copy
import numpy as np

class Machine(object):

    def __init__(self, id):
        self.id = id
        self.jobs = []
        self.total_completion_time = 0
    
    def __repr__(self):
        repr = "--- Machine {} --- \n".format(self.id)
        repr += "total_completion_time: {} \n".format(self.get_total_completion_time())

        if self.jobs:
            repr += "Job ID: "
            for j in self.jobs:
                repr += str(j.id) + ", "
        repr += "\n"
        return str(self.id)
            
    def get_total_completion_time(self) -> int:
        total_makespan = 0
        number_of_jobs = len(self.jobs)
        if self.total_completion_time == 0:
            for i in range(number_of_jobs):

                cmax = 0
                for a in range(i):
                    cmax += self.jobs[a].process_time

                self.jobs[i].makespan = (cmax + self.jobs[i].process_time) * self.jobs[i].weight
                del cmax
                total_makespan += self.jobs[i].makespan
            self.total_completion_time = total_makespan
        
        del total_makespan
        del number_of_jobs
        return self.total_completion_time
    
    def get_total_completion_time_2(self) -> int:
        
        total = 0

        for job in self.jobs:
            total += job.OUT * job.weight

        return total

    def get_Cmax(self) -> int:
        total = 0
        for job in self.jobs:
            total += np.sum(job.process_time) + job.idle
        
        return total
    
    def get_Cmax_2(self) -> int:
        total = 0
        for job in self.jobs:
            total += job.OUT * job.weight

class Job(object):

    def __init__(self, id, process_time, weight = 1):
        self.id = id
        self.process_time = process_time
        self.completion_time = 0
        self.machine: Machine = None
        self.weight = weight
        self.weight_ratio = np.divide(weight, np.sum(process_time))
        self.makespan = 0
        self.IN = 0
        self.OUT = 0
        self.idle = 0

    def __repr__(self): 
    
        str = "--- Job {} --- \n".format(self.id)
        str += "process_time: {} \n".format(self.process_time)
        if self.machine:
            str += "Machine ID: {}\n".format(self.machine.id)
        return str


    def __lt__(self, other):
        return np.sum(self.process_time) < np.sum(other.process_time)
 

class Result():

    def __init__(self, machines, Cmax_machine: Machine, total_completion_time, Cmax=0):
        self.machines = machines
        self.Cmax = Cmax
        self.Cmax_machine = Cmax_machine
        self.total_completion_time = total_completion_time

