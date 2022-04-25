import pickle
import geopy.distance
import networkx as nx
import osmnx as ox
import tqdm
#ox.config(use_cache=True, log_console=False)
import warnings
warnings.filterwarnings("ignore")
import os
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
import argparse

parser = argparse.ArgumentParser(description="Train and predict using the MONAV-CH model.")
parser.add_argument("--dataset", help="Specify the dataset to use", default="geolife")
parser.add_argument("--W", help="The threshold ratio of total distance over minimum path distance", default="25")
parser.add_argument("--D0", help="D0", default="1000000")
parser.add_argument("--D1", help="D1", default="1000000")
args = parser.parse_args()

dataset = args.dataset
W = int(args.W)
D0 = int(args.D0)
D1 = int(args.D1)
data_file = "trajectories_labeled_" + dataset + ".pkl"
all_data = pickle.load(open(data_file, "rb"))

X = [t[0] for t in all_data]
y = [t[1] for t in all_data]
X = [[p[:2][::-1] for p in t] for t in X]

def trajectory_distance(traj):
    dist = 0.0
    for i in range(len(traj) - 1):
        dist += geopy.distance.great_circle(traj[i], traj[i+1]).meters
    return dist

def get_nearest_nodes(G, start, finish):
    start = [round(start[0], 6), round(start[1], 6)]
    finish = [round(finish[0], 6), round(finish[1], 6)]
    orig_node = ox.get_nearest_node(G, start)
    target_node = ox.get_nearest_node(G, finish)

    return orig_node, target_node

def snapping_distance(G, start, finish, orig_node, target_node):
    start_yx = [G.nodes[orig_node]['y'], G.nodes[orig_node]['x']]
    end_yx = [G.nodes[target_node]['y'], G.nodes[target_node]['x']]
    snap_start = geopy.distance.great_circle(start_yx, start).meters
    snap_end = geopy.distance.great_circle(end_yx, finish).meters

    return max(snap_start, snap_end)

def shortest_path(G, start, finish):  
    try:
        length = nx.shortest_path_length(G=G, source=start, target=finish, weight="length")
        return length
    except Exception as e:
        print(e)
        return 10000

dists = []
if os.path.exists("monav_dists_"+dataset+".pkl"):
    dists = pickle.load(open("monav_dists_"+dataset+".pkl", "rb"))
else:
    # get a graph
    G = ox.graph_from_place("Beijing, China", network_type='drive', simplify=True)

    # impute missing edge speed and add travel times
    G = ox.add_edge_speeds(G)
    G = ox.add_edge_travel_times(G)

    i = 0
    for trajectory in tqdm.tqdm(X):
        dist = trajectory_distance(trajectory)

        orig_node, target_node = get_nearest_nodes(G, trajectory[0], trajectory[-1])

        shortest = shortest_path(G, orig_node, target_node)
        ratio = 0
        if shortest > 0:
            ratio = dist/shortest

        snap_dist = snapping_distance(G, trajectory[0], trajectory[-1], orig_node, target_node)
        
        dists.append((trajectory, (snap_dist, dist, ratio), y[i]))
        i += 1
    pickle.dump(dists, open("monav_dists_"+dataset+".pkl", "wb"))

def evaluate(x):
    if x[1][2] > W or x[1][0] > D0 or x[1][1] > D1:
        return 1
    else:
        return 0

y_pred = [evaluate(d) for d in dists]

print("Accuracy score:", accuracy_score(y, y_pred))
print("F1 score:", f1_score(y, y_pred, average="macro"))
print(confusion_matrix(y, y_pred))
