import subprocess
import numpy as np

params = [
    [5, 0.03, 5], [5, 0.03, 10], [5, 0.03, 15], [5, 0.03, 20],
    [5, 0.05, 5], [5, 0.05, 10], [5, 0.05, 15], [5, 0.05, 20],
    [8, 0.03, 5], [8, 0.03, 10], [8, 0.03, 15], [8, 0.03, 20],
    [8, 0.05, 5], [8, 0.05, 10], [8, 0.05, 15], [8, 0.05, 20],
    [10, 0.03, 5], [10, 0.03, 10], [10, 0.03, 15], [10, 0.03, 20],
    [10, 0.05, 5], [10, 0.05, 10], [10, 0.05, 15], [10, 0.05, 20],
    [12, 0.03, 5], [12, 0.03, 10], [12, 0.03, 15], [12, 0.03, 20],
    [12, 0.05, 5], [12, 0.05, 10], [12, 0.05, 15], [12, 0.05, 20],
]

def average(arr):
    return np.average(arr, 0)

for param_set in params:
    print(param_set)
    output = subprocess.check_output(f"python3 ProposedApproach/AutomaticLabeling.py --G {param_set[0]} --thr {param_set[1]} --minThr {param_set[2]}", shell=True).decode("utf-8")
    lines = output.split("\n")
    g_len = round(float(lines[7].split(":")[1]), 3)
    sil = round(float(lines[12].split(":")[1]), 3)
    ratio = round(int(lines[-2].split(":")[1])/16170, 3)
    print(param_set[0], "&", param_set[1], "&", param_set[2], "&", ratio, "&", sil, "&", g_len, "\\\\")
    print("\\hline")

'''
5 & 0.03 & 5 & 0.027 & 0.922 & 2.385 \\
\hline
5 & 0.03 & 10 & 0.037 & 0.932 & 2.385 \\
\hline
5 & 0.03 & 15 & 0.047 & 0.958 & 2.385 \\
\hline
5 & 0.03 & 20 & 0.056 & 0.968 & 2.385 \\
\hline
5 & 0.05 & 5 & 0.031 & 0.922 & 2.385 \\
\hline
5 & 0.05 & 10 & 0.042 & 0.932 & 2.385 \\
\hline
5 & 0.05 & 15 & 0.052 & 0.958 & 2.385 \\
\hline
5 & 0.05 & 20 & 0.061 & 0.968 & 2.385 \\
\hline
8 & 0.03 & 5 & 0.069 & 0.889 & 3.998 \\
\hline
8 & 0.03 & 10 & 0.093 & 0.909 & 3.998 \\
\hline
8 & 0.03 & 15 & 0.108 & 0.923 & 3.998 \\
\hline
8 & 0.03 & 20 & 0.125 & 0.936 & 3.998 \\
\hline
8 & 0.05 & 5 & 0.088 & 0.889 & 3.998 \\
\hline
8 & 0.05 & 10 & 0.112 & 0.909 & 3.998 \\
\hline
8 & 0.05 & 15 & 0.127 & 0.923 & 3.998 \\
\hline
8 & 0.05 & 20 & 0.144 & 0.936 & 3.998 \\
\hline
10 & 0.03 & 5 & 0.076 & 0.84 & 4.91 \\
\hline
10 & 0.03 & 10 & 0.11 & 0.89 & 4.91 \\
\hline
10 & 0.03 & 15 & 0.131 & 0.896 & 4.91 \\
\hline
10 & 0.03 & 20 & 0.142 & 0.902 & 4.91 \\
\hline
10 & 0.05 & 5 & 0.102 & 0.84 & 4.91 \\
\hline
10 & 0.05 & 10 & 0.135 & 0.89 & 4.91 \\
\hline
10 & 0.05 & 15 & 0.156 & 0.896 & 4.91 \\
\hline
10 & 0.05 & 20 & 0.167 & 0.902 & 4.91 \\
\hline
12 & 0.03 & 5 & 0.097 & 0.847 & 5.126 \\
\hline
12 & 0.03 & 10 & 0.135 & 0.885 & 5.126 \\
\hline
12 & 0.03 & 15 & 0.159 & 0.894 & 5.126 \\
\hline
12 & 0.03 & 20 & 0.182 & 0.907 & 5.126 \\
\hline
12 & 0.05 & 5 & 0.118 & 0.847 & 5.126 \\
\hline
12 & 0.05 & 10 & 0.156 & 0.885 & 5.126 \\
\hline
12 & 0.05 & 15 & 0.18 & 0.894 & 5.126 \\
\hline
12 & 0.05 & 20 & 0.203 & 0.907 & 5.126 \\
\hline
'''