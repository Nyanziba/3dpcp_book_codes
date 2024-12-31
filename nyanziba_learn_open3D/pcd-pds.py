import open3d as o3d
import random
import math
import numpy as np
import argparse

import open3d as o3d
import random
import math
import numpy as np
import argparse

def poisson_disk_sampling_3d(points, min_distance, num_candidates=30):
    """
    3次元データに対するPoisson Disk Sampling
    :param points: 入力点群（N x 3のnumpy配列）
    :param min_distance: 最小距離
    :param num_candidates: 候補点の生成数
    :return: サンプリングされた点群
    """
    # 既存点群をリストに変換
    samples = [points[random.randint(0, len(points) - 1)]]
    active_list = [samples[0]]
    min_distance2 = min_distance ** 2  # 距離の二乗を計算しておく

    while active_list:
        # アクティブリストからランダムに1点を選ぶ
        active_index = random.randint(0, len(active_list) - 1)
        active_point = active_list[active_index]
        print(len(active_list))
        # 候補点を生成
        found_new_point = False
        for _ in range(num_candidates):
            # ランダムな方向と距離で新しい点を生成
            direction = np.random.normal(size=3)
            direction /= np.linalg.norm(direction)
            distance = min_distance * (1 + random.random())
            new_point = active_point + direction * distance
            # 新しい点が既存の点と十分に離れているか確認
            if np.all(np.linalg.norm(points - new_point, axis=1) >= min_distance):
                samples.append(new_point)
                active_list.append(new_point)
                found_new_point = True
                break

        # 新しい点が見つからなければアクティブリストから削除
        if not found_new_point:
            active_list.pop(active_index)

    return np.array(samples)

argparse = argparse.ArgumentParser(description='Poisson disk sampling')
argparse.add_argument('filename', type=str, help='Point cloud file to read')
argparse.add_argument('min_distance', type=float, help='Minimum distance')
args = argparse.parse_args()
filename = args.filename
min_distance = args.min_distance
# 入力データの読み込み
pcd = o3d.io.read_point_cloud(filename)
print(pcd)
o3d.visualization.draw_geometries([pcd])
pcd = pcd.voxel_down_sample(voxel_size=min_distance)
print(pcd)
o3d.visualization.draw_geometries([pcd])
points = np.asarray(pcd.points)
print(points)
# Poisson Disk Samplingを適用#
sampled_points = poisson_disk_sampling_3d(points, min_distance+1.0)

# サンプリング結果を点群として保存・描画
sampled_pcd = o3d.geometry.PointCloud()
sampled_pcd.points = o3d.utility.Vector3dVector(sampled_points)
print(sampled_pcd)
# 可視化
o3d.visualization.draw_geometries([sampled_pcd])
