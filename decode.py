import os
import json

lines = []

for dir1 in os.listdir("Datasets/ThessalonikiDataset/data"):
    for file in os.listdir("Datasets/ThessalonikiDataset/data/"+dir1+"/"):
        for line in open("Datasets/ThessalonikiDataset/data/"+dir1+"/"+file, "r").readlines():
            lines.append(line)

print(len(lines))

data = []
for line in lines:
    obj = json.loads(line)
    data.append(obj["frame"])

#print(data[:3])
with open("encoded.txt", "w") as file:
    for d in data:
        file.write(d+"\n")
