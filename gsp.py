import subprocess
import numpy as np

params = [0.05, 0.10, 0.15, 0.20]

def average(arr):
    return np.average(arr, 0)

for param in params:
    print(param)
    numbers = []
    
    for seed in range(100, 105):
        output = subprocess.check_output(f"python3 ProposedApproach/Proposed.py --C 8000 --gamma scale --kernel rbf --method svm --do_gsp 1 --gsp_support {param} --seed {seed}", shell=True)
        last4 = output.decode("utf-8").replace("seconds", "").split("\n")[-7:-3]
        print(last4)
        last4numbers = [round(float(x.split(":")[-1]), 3) for x in last4]
        numbers.append(last4numbers)
    avg = average(np.array(numbers))
    print(param, "&", avg[0], "&", avg[1], "&", avg[2], "&", avg[3], "\\\\")
    print("\\hline")
