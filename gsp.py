import subprocess
import numpy as np

params = [
    #0.05, 
    #0.10, 
    #0.15, 
    #0.20,
    #0.25,
    0.30
]

def average(arr):
    return np.average(arr, 0)

for param in params:
    print(param)
    numbers = []
    
    for seed in range(100, 105):
        output = subprocess.check_output(f"python3 ProposedApproach/Proposed.py --C 8000 --gamma scale --kernel rbf --method svm --do_gsp 1 --gsp_support {param} --seed {seed}", shell=True)
        last4 = output.decode("utf-8").replace("seconds", "").split("\n")[-7:-3]
        last4numbers = [round(float(x.split(":")[-1]), 3) for x in last4]
        numbers.append(last4numbers)
    avg = average(np.array(numbers))
    print(param, "&", avg[0], "&", avg[1], "&", avg[2], "&", avg[3], "\\\\")
    print("\\hline")

'''
0.05
0.05 & 0.9884000000000001 & 0.9284000000000001 & 0.9765999999999998 & 0.8518000000000001 \\
\hline
0.1
0.1 & 0.9882 & 0.9254000000000001 & 0.9763999999999999 & 0.8489999999999999 \\
\hline
TODO
0.15
0.15 & 0.9722 & 0.8732 & 0.9582 & 0.8036 \\
\hline
0.2
0.2 & 0.9716000000000001 & 0.8699999999999999 & 0.9578 & 0.8024000000000001 \\
\hline
'''