import sys
import open3d as o3d
import argparse
argparse = argparse.ArgumentParser(description='Poisson disk sampling')
argparse.add_argument('filename', type=str, help='Triangle mesh file to read')
argparse.add_argument('k', type=int, help='Number of points to downsample')
args = argparse.parse_args()
filename = args.filename
k = args.k
print("Loading a triangle mesh from", filename)
mesh = o3d.io.read_triangle_mesh(filename)
print(mesh)

o3d.visualization.draw_geometries([mesh], mesh_show_wireframe=True)

downpcd = mesh.sample_points_poisson_disk(number_of_points=k)
print(downpcd)

o3d.visualization.draw_geometries([downpcd])
