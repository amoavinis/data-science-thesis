import subprocess
import numpy as np

params = [
    #[30, 0.5], [30, 1.0], [30, 1.5], [30, 2.0], [30, 2.5], [30, 3.0],
    #[40, 0.5], [40, 1.0], [40, 1.5], [40, 2.0], [40, 2.5], 
    [40, 3.0],
    [50, 0.5], [50, 1.0], [50, 1.5], [50, 2.0], [50, 2.5], [50, 3.0],
]

def average(arr):
    return np.average(arr, 0)

for param_set in params:
    print(param_set)
    numbers = []
    
    for seed in range(100, 105):
        output = subprocess.check_output(f"python3 ProposedApproach/Proposed.py --G {param_set[0]} --eps {param_set[1]} --method cluster --seed {seed}", shell=True)
        last4 = output.decode("utf-8").replace("seconds", "").split("\n")[-7:-3]
        #print(last4)
        last4numbers = [round(float(x.split(":")[-1]), 3) for x in last4]
        numbers.append(last4numbers)
    avg = average(np.array(numbers))
    print(param_set[0], "&", param_set[1], "&", avg[0], "&", avg[1], "&", avg[2], "&", avg[3], "\\\\")
    print("\\hline")
