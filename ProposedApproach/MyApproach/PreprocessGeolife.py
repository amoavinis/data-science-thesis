import os
import geopy.distance
from sklearn.metrics import silhouette_score
from CustomScaler import Scaler
from sklearn.preprocessing import MinMaxScaler
import datetime
from fastcluster import linkage
from scipy.cluster.hierarchy import fcluster
from scipy.spatial import distance
from tqdm import tqdm
import pickle
from math import sqrt
import numpy as np

class Preprocessor:
    def __init__(self):
        self.all_trajectories = []
        self.paths = []
        self.dist_clustering = 0.1
        self.inliers = []
        self.outliers = []

    def distance_of_transition(self, transition):
        return geopy.distance.great_circle(list(reversed(transition[0])), list(reversed(transition[1]))).meters

    def distance_of_trajectory(self, traj):
        dist = 0.0
        for i in range(len(traj) - 1):
            dist += self.distance_of_transition([traj[i][:2], traj[i+1][:2]])
        return dist

    def speeds_in_traj(self, traj):
        speeds = []
        for i in range(len(traj)-1):
            dx = self.distance_of_transition([traj[i][:2], traj[i+1][:2]])
            dt = traj[i+1][2] - traj[i][2]
            if dt > 0:
                speeds.append(dx/dt)
        return {
            'min_speed': min(speeds),
            'max_speed': max(speeds),
            'avg_speed': sum(speeds)/len(speeds)
        }

    def slant(self, traj):
        sd_len = sqrt((traj[-1][1]-traj[0][1])**2 + (traj[-1][0]-traj[0][0])**2)
        dx = traj[-1][0] - traj[0][0]
        if sd_len > 0:
            sine = dx / sd_len
            return sine
        else:
            return 0

    def group_by_sd_pairs(self, trajectories, threshold):
        sd_pairs = dict()
        for traj in trajectories:
            s = traj[1][0]
            d = traj[1][-1]
            sd_pair = s+"->"+d
            if sd_pair in sd_pairs:
                sd_pairs[sd_pair].append(traj)
            else:
                sd_pairs[sd_pair] = [traj]
        filtered_dict = dict()
        for sd in sd_pairs:
            if len(sd_pairs[sd]) >= threshold:
                filtered_dict[sd] = sd_pairs[sd]
            else:
                self.outliers.extend([t[0] for t in sd_pairs[sd]])

        return filtered_dict

    def intersection(self, lst1, lst2):
        return set(lst1).intersection(lst2)

    def union(self, lst1, lst2):
        return set(lst1).union(lst2)

    def custom_distance(self, x1, x2):
        X1 = set(self.paths[int(x1[0])])
        X2 = set(self.paths[int(x2[0])])
        jaccard_sq = 1 - len(X1.intersection(X2))/len(X1.union(X2))
        return jaccard_sq

    def clustering_trajectories(self):
        filtered_sd = self.group_by_sd_pairs(self.all_trajectories, 2)
        print("Total number of trajectories:", len(self.all_trajectories))
        print("Number of step 1 outliers:", len(self.outliers))
        score = []
        for k in filtered_sd:
            self.paths = [f[1] for f in filtered_sd[k]]
            to_cluster = [[i] for i in range(len(self.paths))]
            linked = linkage(to_cluster, method='complete', metric=self.custom_distance)
            clusters = fcluster(linked, t=self.dist_clustering, criterion='distance')
            if len(set(clusters)) >= 2 and len(set(clusters)) <= len(to_cluster)-1:
                silhouette_score_1 = silhouette_score(to_cluster, clusters, metric=self.custom_distance)
                score.append(silhouette_score_1)

            clusters_grouped = dict()
            for i in range(len(clusters)):
                if clusters[i] in clusters_grouped:
                    clusters_grouped[clusters[i]].append(filtered_sd[k][i])
                else:
                    clusters_grouped[clusters[i]] = [filtered_sd[k][i]]
            for cluster in clusters_grouped:
                if len(clusters_grouped[cluster])/len(filtered_sd[k]) > 0.03:
                    self.inliers.extend([t[0] for t in clusters_grouped[cluster]])
                else:
                    self.outliers.extend([t[0] for t in clusters_grouped[cluster]])
        print("Average silhouette score:", sum(score)/len(score))

    def trajectories_to_pickle(self):
        res = []
        for inlier in self.inliers:
            res.append((inlier, 0))
        for outlier in self.outliers:
            res.append((outlier, 1))
        pickle.dump(res, open(os.getcwd()+'/trajectories_labeled.pkl', 'wb'))

    def preprocess(self):
        print("Reading trajectories from disk...")
        self.all_trajectories = pickle.load(open("trajectories_with_grid.pkl", "rb"))
        print("Read trajectories from disk.")
        print("Clustering trajectories...")
        self.clustering_trajectories()
        print("Clustered trajectories.")
        self.trajectories_to_pickle()
        print("Trajectories output to trajectories_labeled.pkl")
        print("Total number of inliers:", len(self.inliers))
        print("Total number of outliers:", len(self.outliers))

p = Preprocessor()
p.preprocess()
