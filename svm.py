import subprocess
import numpy as np

params = [
    [1, 'scale', 'rbf'], 
    [10, 'scale', 'rbf'], 
    [100, 'scale', 'rbf'], 
    #[1000, 'scale', 'rbf'], 
    #[2000, 'scale', 'rbf'], 
    #[4000, 'scale', 'rbf'],
    #[4000, 'auto', 'rbf'], 
    [4000, 'scale', 'sigmoid'], 
    [4000, 'auto', 'sigmoid'], 
    #[8000, 'scale', 'rbf'], 
    #[8000, 'auto', 'rbf'], 
    [8000, 'scale', 'sigmoid'], 
    [8000, 'auto', 'sigmoid']
]

def average(arr):
    return np.average(arr, 0)

for param_set in params:
    print(param_set)
    numbers = []
    
    for seed in range(100, 105):
        output = subprocess.check_output(f"python3 ProposedApproach/Proposed.py --C {param_set[0]} --gamma {param_set[1]} --kernel {param_set[2]} --method svm --seed {seed}", shell=True)
        last4 = output.decode("utf-8").replace("seconds", "").split("\n")[-7:-3]
        #print(last4)
        last4numbers = [round(float(x.split(":")[-1]), 3) for x in last4]
        numbers.append(last4numbers)
    avg = average(np.array(numbers))
    print(param_set[0], "&", param_set[1], "&", param_set[2], "&", avg[0], "&", avg[1], "&", avg[2], "&", avg[3], "\\\\")
    print("\\hline")

