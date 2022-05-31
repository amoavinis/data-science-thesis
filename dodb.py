import subprocess
import numpy as np

params = [
    #[2, 100000000, 100000000],
    #[5, 100000000, 100000000],
    #[8, 100000000, 100000000],
    #[10, 100000000, 100000000],
    #[15, 100000000, 100000000],
    #[20, 100000000, 100000000],
    [15, 200, 100000000],
    [15, 500, 100000000],
    [15, 1000, 100000000],
    [15, 100000000, 20000],
    [15, 100000000, 30000],
    [15, 100000000, 40000],
    [15, 100000000, 50000],
]


def average(arr):
    return np.average(arr, 0)


for param_set in params:
    print(param_set)
    numbers = []
    t = 0
    for seed in range(100, 105):
        output = subprocess.check_output(
            f"python3 DODB/DODB.py --W {param_set[0]} --D0 {param_set[1]} --D1 {param_set[2]} --seed {seed}",
            shell=True)
        last2 = output.decode("utf-8").split("\n")[:2]
        last2numbers = [round(float(x.split(":")[-1]), 3) for x in last2]
        numbers.append(last2numbers)
    avg = average(np.array(numbers))
    print(param_set[0], "&", param_set[1], "&", param_set[2], "&",
          avg[0], "&", avg[1], "\\\\")
    print("\\hline")
'''
15 & 200 & 100000000 & 0.7888000000000001 & 0.58 \\
\hline
15 & 500 & 100000000 & 0.8996000000000001 & 0.6746000000000001 \\
\hline
15 & 1000 & 100000000 & 0.9018 & 0.6748000000000001 \\
\hline
[15, 100000000, 20000]
15 & 100000000 & 20000 & 0.8122 & 0.6554 \\
\hline
[15, 100000000, 30000]
15 & 100000000 & 30000 & 0.8804000000000001 & 0.7162 \\
\hline
[15, 100000000, 40000]
15 & 100000000 & 40000 & 0.8981999999999999 & 0.724 \\
\hline
[15, 100000000, 50000]
15 & 100000000 & 50000 & 0.9028 & 0.7154 \\
\hline
'''