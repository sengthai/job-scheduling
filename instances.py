from Model import Job, Machine
import random


def get_instance(seed = 1, has_weight = False):

    random.seed(seed * 5)

    while True:
        num_of_machines = random.randint(3, 5)  # set random number of machince from 3 to 5
        num_of_jobs = random.randint(6, 8)     # set random number of jobs from 6 to 10
        if num_of_machines < num_of_jobs:
            break

    if has_weight:
        jobs = [ Job(i, random.randint(4, 25), random.randint(4, 25)) for i in range(num_of_jobs) ]
    else:
        jobs = [ Job(i, random.randint(4, 25)) for i in range(num_of_jobs) ]
    
    machines = [ Machine(i) for i in range(num_of_machines) ]

    return (jobs, machines)
