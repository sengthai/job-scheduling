from tabulate import tabulate
from instances import get_instance
from Model import Job, Machine, Result
from copy import copy



def draw(machines, info: bool = False):
    str = ""

    for m in machines:
        str += __get_machine(m) + '\n'

    
    print(str)

def draw_table(jobs):
    job_ids = ['j{}'.format(i.id) for i in jobs]
    process_times = [ i.process_time for i in jobs]
    weights = [ i.weight for i in jobs]

    table = [ job_ids, process_times]
    if weights[0] != 1:
        table.append(weights)
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

def draw_series_job(jobs):

    arrow = " => "
    str = "=============== Jobs series ================\n"
    ids = [ job.id for job in jobs]

    while (ids):

        str += arrow + "| {} |".format(ids[0])
        
        del ids[0]

    str += "\n"
    print(str)

def draw_Cmax(id, Cmax):
    str = "The Cmax is M{}: {} \n".format(id, Cmax)
    print(str)

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

    for i in range(job.idle):
        time += " "

    process_time = j.process_time

    # if process_time > 10:
    #     process_time = process_time - 1

    for i in range(process_time):
        if i == int(process_time/2):
            time += str(job.id)
        else:
            time += sym

    return time

    