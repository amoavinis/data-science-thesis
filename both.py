import subprocess
import numpy as np

def average(arr):
    return np.average(arr, 0)


numbers = []

for seed in range(100, 105):
    output = subprocess.check_output(f"python3 ProposedApproach/Proposed.py --C 4000 --gamma scale --kernel rbf --method both --seed {seed}", shell=True)
    last4 = output.decode("utf-8").replace("seconds", "").split("\n")[-7:-3]
    #print(last4)
    last4numbers = [round(float(x.split(":")[-1]), 3) for x in last4]
    numbers.append(last4numbers)
avg = average(np.array(numbers))
print(avg[0], "&", avg[1], "&", avg[2], "&", avg[3], "\\\\")
print("\\hline")

'''
0.9576 & 0.8151999999999999 & 0.9461999999999999 & 0.7672000000000001 \\
\hline
'''