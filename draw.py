from tabulate import tabulate
from instances import get_instance
from Model import Job, Machine
from copy import copy



def draw(machines, info: bool = False):
    str = ""

    for m in machines:
        str += __get_machine(m) + '\n'
    if info:
        str += __get_info(machines)
    
    print(str)

def draw_table(jobs):
    job_ids = ['j{}'.format(i.id) for i in jobs]
    process_times = [ i.process_time for i in jobs]
    weights = [ i.weight for i in jobs]

    table = [ job_ids, process_times]
    if weights[0] != 1:
        table.append(weights)
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

def __get_info(machines):
    
    str = "\n===== Total Completion times ======\n"
    Cmax = [0, 0]
    for m in machines:
        c = m.get_total_completion_time()

        if c > Cmax[1]: Cmax = [m.id, c]

        str += "M{}: {} \n".format(m.id, m) 

    str += "The Cmax is M{}: {} \n".format(Cmax[0], Cmax[1])
    str += "====================================\n"
    return str


def __get_machine(machine: Machine):
    jobs = machine.jobs
    str = "M{} : ".format(machine.id)
    for idx, j in enumerate(jobs):
        str += __get_jobs(j, idx)
    
    return str
    
def __get_jobs(job: Job, format):
    sym0 = "▒"
    sym1 = "▓"
    time = ""

    if format%2 == 0:
        sym = sym0
    else:
        sym = sym1

    j = copy(job)

    process_time = j.process_time

    if process_time > 10:
        process_time = process_time - 1

    for i in range(process_time):
        if i == int(process_time/2):
            time += str(job.id)
        else:
            time += sym

    return time
