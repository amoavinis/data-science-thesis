import os
import json
from random import sample, seed

lines = []

for dir1 in os.listdir("Datasets/ThessalonikiDataset2G/data"):
    for file in os.listdir("Datasets/ThessalonikiDataset2G/data/"+dir1+"/"):
        for line in open("Datasets/ThessalonikiDataset2G/data/"+dir1+"/"+file, "r").readlines():
            lines.append(line)

print(len(lines))
seed(100)

lines = sample(lines, 100000)

data = []
for line in lines:
    obj = json.loads(line)
    data.append(obj["frame"])

#print(data[:3])
with open("encoded2G.txt", "w") as file:
    for d in data:
        file.write(d+"\n")
