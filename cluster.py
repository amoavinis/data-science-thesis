import subprocess
import numpy as np

params = [
    #[30, 0.5], 
    #[30, 1.0], [30, 1.5], [30, 2.0], #[30, 2.5], [30, 3.0],
    #[40, 0.5], 
    #[40, 1.0], [40, 1.5], [40, 2.0], #[40, 2.5], [40, 3.0], 
    #[50, 0.5], 
    #[50, 1.0], [50, 1.5], [50, 2.0], 
    #[50, 2.5], [50, 3.0],
    [20, 1.0], [20, 1.5], [20, 2.0]
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


'''
[20, 1.0]
20 & 1.0 & 0.9505999999999999 & 0.6900000000000001 & 0.9568 & 0.6914 \\
\hline
[20, 1.5]
20 & 1.5 & 0.9551999999999999 & 0.6522 & 0.9582 & 0.6504000000000001 \\
\hline
[20, 2.0]
20 & 2.0 & 0.9554 & 0.5889999999999999 & 0.9560000000000001 & 0.5624 \\
\hline
[30, 1.0]
30 & 1.0 & 0.925 & 0.6856 & 0.9366000000000001 & 0.7081999999999999 \\
\hline
[30, 1.5]
30 & 1.5 & 0.9442 & 0.7048 & 0.9513999999999999 & 0.7133999999999999 \\
\hline
[30, 2.0]
30 & 2.0 & 0.9534 & 0.6874 & 0.9574 & 0.6866 \\
\hline
[40, 1.0]
40 & 1.0 & 0.8879999999999999 & 0.6462000000000001 & 0.9002000000000001 & 0.6610000000000001 \\
\hline
[40, 1.5]
40 & 1.5 & 0.9184000000000001 & 0.6768000000000001 & 0.9276 & 0.6868000000000001 \\
\hline
[40, 2.0]
40 & 2.0 & 0.9406000000000001 & 0.6964 & 0.9484 & 0.7091999999999999 \\
\hline
[50, 1.0]
50 & 1.0 & 0.8575999999999999 & 0.6194 & 0.8710000000000001 & 0.6298 \\
\hline
[50, 1.5]
50 & 1.5 & 0.8897999999999999 & 0.6462 & 0.9006000000000001 & 0.6614000000000001 \\
\hline
[50, 2.0]
50 & 2.0 & 0.923 & 0.6808000000000001 & 0.9314 & 0.692 \\
\hline
DONE
30 & 0.5 & 0.7710000000000001 & 0.5996 & 0.7956000000000001 & 0.613 \\
\hline
30 & 1.0 & 0.9218 & 0.7146 & 0.9236000000000001 & 0.6988 \\
\hline
30 & 1.5 & 0.9320000000000002 & 0.6966 & 0.9318000000000002 & 0.6766 \\
\hline
30 & 2.0 & 0.9359999999999999 & 0.655 & 0.9378 & 0.6482 \\
\hline
30 & 2.5 & 0.9366 & 0.6115999999999999 & 0.9354000000000001 & 0.5921999999999998 \\
\hline
30 & 3.0 & 0.9356 & 0.5673999999999999 & 0.9338000000000001 & 0.5454000000000001 \\
\hline
40 & 0.5 & 0.7118 & 0.5558000000000001 & 0.7434 & 0.576 \\
\hline
40 & 1.0 & 0.8956 & 0.7001999999999999 & 0.8984 & 0.6902000000000001 \\
\hline
[40, 1.5]
40 & 1.5 & 0.9182 & 0.7138 & 0.9199999999999999 & 0.6974 \\
\hline
[40, 2.0]
40 & 2.0 & 0.9314 & 0.704 & 0.9326000000000001 & 0.6914 \\
\hline
[40, 2.5]
40 & 2.5 & 0.9348000000000001 & 0.6718000000000001 & 0.9356 & 0.6564000000000001 \\
\hline
[40, 3.0]
40 & 3.0 & 0.9350000000000002 & 0.6216 & 0.9368000000000001 & 0.6182000000000001 \\
\hline
[50, 0.5]
50 & 0.5 & 0.6644000000000001 & 0.5258 & 0.6932 & 0.5438000000000001 \\
[50, 1.0]
50 & 1.0 & 0.8676 & 0.6742000000000001 & 0.873 & 0.6686000000000001 \\
\hline
[50, 1.5]
50 & 1.5 & 0.8954000000000001 & 0.6963999999999999 & 0.8972000000000001 & 0.6860000000000002 \\
\hline
[50, 2.0]
50 & 2.0 & 0.9198000000000001 & 0.7108 & 0.9221999999999999 & 0.7001999999999999 \\
\hline
[50, 2.5]
50 & 2.5 & 0.9305999999999999 & 0.7068 & 0.9301999999999999 & 0.6858 \\
\hline
[50, 3.0]
50 & 3.0 & 0.9339999999999999 & 0.6766 & 0.9358000000000001 & 0.6626000000000001 \\
\hline
'''