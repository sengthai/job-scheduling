
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
    
    def get_Cmax(self) -> int:
        total = 0
        for job in self.jobs:
            total += job.process_time
        
        return total

class Job(object):

    def __init__(self, id, process_time, weight = 1):
        self.id = id
        self.process_time = process_time
        self.completion_time = 0
        self.machine: Machine = None
        self.weight = weight
        self.weight_ratio = weight / process_time
        self.makespan = 0

    def __repr__(self): 
    
        str = "--- Job {} --- \n".format(self.id)
        str += "process_time: {} \n".format(self.process_time)
        if self.machine:
            str += "Machine ID: {}\n".format(self.machine.id)
        return str


    def __lt__(self, other):
        return self.process_time < other.process_time


class Result():

    def __init__(self, machines, Cmax_machine: Machine, total_completion_time):
        self.machines = machines
        self.Cmax = Cmax_machine.get_Cmax()
        self.Cmax_machine = Cmax_machine
        self.total_completion_time = total_completion_time
