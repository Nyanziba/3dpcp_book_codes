import numpy as np
import open3d as o3d
import copy

# rosとかにあるTFの3軸が作られる。
mesh = o3d.geometry.TriangleMesh.create_coordinate_frame()

#回転行列の作成
#オイラー角を使って回転行列を作成する。
R = o3d.geometry.get_rotation_matrix_from_xyz([0, np.pi/2, 0])
print("R:",np.round(R,7))
#回転行列を使って、meshを回転させる。こちらは角度。
R = o3d.geometry.get_rotation_matrix_from_axis_angle([0,np.pi/2,0])
print("R:",np.round(R,7))
#クォータニオンを使って回転行列を作成する。open3dはクォータにオンのパラメータは、w,x,y,zの順番。
R = o3d.geometry.get_rotation_matrix_from_quaternion([np.cos(np.pi/5),0,np.sin(np.pi/5),0])
print("R:",np.round(R,7))
mesh_r = copy.deepcopy(mesh)
## デフォルトの回転中心は重心の位置。
mesh_r.rotate(R, center=(0, 0, 0))

#並進行列の作成
t = np.array([1, 2, 3])
mesh_t = copy.deepcopy(mesh).translate(t)
o3d.visualization.draw_geometries([mesh, mesh_r, mesh_t])

#回転+並進行列の作成
T = np.eye(4)
T[:3, :3] = R
T[:3, 3] = t
print("T:",np.round(T,7))
mesh_rt = copy.deepcopy(mesh).transform(T)
o3d.visualization.draw_geometries([mesh, mesh_r, mesh_t, mesh_rt])

#スケール
mesh_s = copy.deepcopy(mesh).scale(0.5, center=mesh.get_center())
o3d.visualization.draw_geometries([mesh, mesh_s])