import sys
import numpy as np
import open3d as o3d
import argparse

def l2_norm(a, b):
    return ((a - b) ** 2).sum(axis=1)

def farthest_point_sampling(pcd, k, metrics=l2_norm):
    indices = np.zeros(k, dtype=np.int32)
    points = np.asarray(pcd.points)
    distances = np.zeros((k, points.shape[0]), dtype=np.float32)
    indices[0] = np.random.randint(len(points))
    farthest_point = points[indices[0]]
    min_distances = metrics(farthest_point, points)
    distances[0, :] = min_distances
    for i in range(1, k):
        indices[i] = np.argmax(min_distances)
        farthest_point = points[indices[i]]
        distances[i, :] = metrics(farthest_point, points)
        min_distances = np.minimum(min_distances, distances[i, :])
    pcd = pcd.select_by_index(indices)
    return pcd

# main
argparse = argparse.ArgumentParser(description='Farthest point sampling')
argparse.add_argument('filename', type=str, help='Point cloud file to read')
argparse.add_argument('k', type=int, help='Number of points to downsample')
args = argparse.parse_args()
filename = args.filename
k = args.k
print("Loading a point cloud from", filename)
pcd = o3d.io.read_point_cloud(filename)
print(pcd)

o3d.visualization.draw_geometries([pcd])
### FPSのdownsamplingが実装されていた。
###つくチャレのPCL地図は30017214点あるので、
# FPSでダウンサンプリングすると、とてつもなく時間がかかる。
downpcd  = pcd.farthest_point_down_sample(k)
print(downpcd)

o3d.visualization.draw_geometries([downpcd])
