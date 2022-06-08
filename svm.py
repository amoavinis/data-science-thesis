import subprocess
import numpy as np

params = [
    [1, 'scale', 'rbf'], 
    [10, 'scale', 'rbf'], 
    [100, 'scale', 'rbf'], 
    [1000, 'scale', 'rbf'], 
    [2000, 'scale', 'rbf'], 
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

'''
[4000, 'scale', 'rbf']
4000 & scale & rbf & 0.983 & 0.8896000000000001 & 0.9763999999999999 & 0.8413999999999999 \\
\hline
[4000, 'auto', 'rbf']
4000 & auto & rbf & 0.9676 & 0.7432 & 0.9682000000000001 & 0.7442 \\
\hline
[8000, 'scale', 'rbf']
8000 & scale & rbf & 0.9838000000000001 & 0.8962 & 0.9766 & 0.844 \\
\hline
[8000, 'auto', 'rbf']
8000 & auto & rbf & 0.9686 & 0.7574 & 0.9693999999999999 & 0.7602 \\
\hline
TODO
[1, 'scale', 'rbf']
1 & scale & rbf & 0.9684999999999999 & 0.756 & 0.969 & 0.747 \\
\hline
[10, 'scale', 'rbf']
10 & scale & rbf & 0.9724999999999999 & 0.7955000000000001 & 0.9715 & 0.7815000000000001 \\
\hline
[100, 'scale', 'rbf']
100 & scale & rbf & 0.977 & 0.8414999999999999 & 0.9744999999999999 & 0.8160000000000001 \\
\hline
[1000, 'scale', 'rbf']
1000 & scale & rbf & 0.981 & 0.8745 & 0.976 & 0.8365 \\
\hline
[2000, 'scale', 'rbf']
2000 & scale & rbf & 0.982 & 0.8815 & 0.976 & 0.839 \\
\hline
[4000, 'scale', 'sigmoid']
4000 & scale & sigmoid & 0.922 & 0.5734999999999999 & 0.924 & 0.5640000000000001 \\
\hline
[4000, 'auto', 'sigmoid']
4000 & auto & sigmoid & 0.934 & 0.6355 & 0.9295 & 0.6085 \\
\hline
[8000, 'scale', 'sigmoid']
8000 & scale & sigmoid & 0.922 & 0.5734999999999999 & 0.924 & 0.5640000000000001 \\
\hline
[8000, 'auto', 'sigmoid']
8000 & auto & sigmoid & 0.934 & 0.639 & 0.93 & 0.6114999999999999 \\
\hline
'''