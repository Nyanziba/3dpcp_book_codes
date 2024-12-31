import sys
import open3d as o3d
import argparse

# Parse arguments
parser = argparse.ArgumentParser(description='Voxelize a point cloud')
parser.add_argument('filename', type=str, help='Point cloud file to read')
parser.add_argument('voxel_size', type=float, help='Voxel size')
args = parser.parse_args()

print("Loading a point cloud from", args.filename)
pcd = o3d.io.read_point_cloud(args.filename)
print(pcd)
o3d.visualization.draw_geometries([pcd])
#o3d.visualization.draw_geometries([pcd], zoom=0.3412,
#                                  front=[0.4257, -0.2125, -0.8795],
#                                  lookat=[2.6172, 2.0475, 1.532],
#                                  up=[-0.0694, -0.9768, 0.2024])

downpcd = pcd.voxel_down_sample(voxel_size=args.voxel_size)
print(downpcd)
#視点移動の設定があったが、うまくいかなかったので削除した。
#視点移動を色々いじることはできるみたいだ。
o3d.visualization.draw_geometries([downpcd])
#o3d.visualization.draw_geometries([downpcd], zoom=0.3412,
#                                  front=[0.4257, -0.2125, -0.8795],
#                                  lookat=[2.6172, 2.0475, 1.532],
#                                  up=[-0.0694, -0.9768, 0.2024])
