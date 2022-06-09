import subprocess
import numpy as np

params = [
    [2, 100000000, 100000000],
    [5, 100000000, 100000000],
    [8, 100000000, 100000000],
    [10, 100000000, 100000000],
    [15, 100000000, 100000000],
    [20, 100000000, 100000000],
    [15, 200, 100000000],
    [15, 500, 100000000],
    [15, 1000, 100000000],
    [15, 500, 20000],
    [15, 500, 30000],
    [15, 500, 40000],
    [15, 500, 50000],
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
DONE
[2, 100000000, 100000000]
2 & 100000000 & 100000000 & 0.7438 & 0.516 \\
\hline
[5, 100000000, 100000000]
5 & 100000000 & 100000000 & 0.8426 & 0.5666 \\
\hline
[8, 100000000, 100000000]
8 & 100000000 & 100000000 & 0.8726 & 0.5858 \\
\hline
[10, 100000000, 100000000]
10 & 100000000 & 100000000 & 0.883 & 0.592 \\
\hline
[15, 100000000, 100000000]
15 & 100000000 & 100000000 & 0.8997999999999999 & 0.6003999999999999 \\
\hline
[20, 100000000, 100000000]
20 & 100000000 & 100000000 & 0.9097999999999999 & 0.6018 \\
\hline
[15, 200, 100000000]
15 & 200 & 100000000 & 0.7786 & 0.5229999999999999 \\
\hline
[15, 500, 100000000]
15 & 500 & 100000000 & 0.8968 & 0.6 \\
\hline
[15, 1000, 100000000]
15 & 1000 & 100000000 & 0.8996000000000001 & 0.6008 \\
\hline
[15, 500, 20000]
15 & 500 & 20000 & 0.7794 & 0.5593999999999999 \\
\hline
[15, 500, 30000]
15 & 500 & 30000 & 0.8526 & 0.6077999999999999 \\
\hline
[15, 500, 40000]
15 & 500 & 40000 & 0.8754000000000002 & 0.6152 \\
\hline
[15, 500, 50000]
15 & 500 & 50000 & 0.8848 & 0.6126 \\
\hline
'''