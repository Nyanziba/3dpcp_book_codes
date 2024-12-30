import sys
import open3d as o3d
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Read a 3d file')
parser.add_argument('filename', type=str, help='3d file to read')


args = parser.parse_args()

print("Loading a point cloud from", args.filename)
pcd = o3d.io.read_point_cloud(args.filename)

print(pcd)
print(np.asarray(pcd.points))
# オフスクリーンレンダリングの設定
vis = o3d.visualization.Visualizer()
vis.create_window(visible=False)  

o3d.visualization.draw_geometries([pcd])

