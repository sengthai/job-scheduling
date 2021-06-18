from Model import Job, Machine
import random


def get_instance(seed = 1, has_weight = False, is_flow_shop = False, num_of_machines = 2, num_of_jobs = 4):

    random.seed(seed * 5)

    if has_weight:
        jobs = [ Job(i, random.randint(4, 7), random.randint(4, 7)) for i in range(num_of_jobs) ]
    else:
        jobs = [ Job(i, random.randint(4, 7)) for i in range(num_of_jobs) ]
    
    if is_flow_shop:
        if has_weight:
            jobs = [ Job(i, [ random.randint(i+1, 7) for i in range(num_of_machines) ], random.randint(4, 20)) for i in range(num_of_jobs) ]
        else:
            jobs = [ Job(i, [ random.randint(i+1, 7) for i in range(num_of_machines) ]) for i in range(num_of_jobs) ]

    machines = [ Machine(i) for i in range(num_of_machines) ]

    return (jobs, machines)
