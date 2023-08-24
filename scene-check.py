from nuscenes.nuscenes import NuScenes
import os

nusc = NuScenes(version='v1.0-trainval', dataroot='/Users/yvonne/work/nuscenes-devkit/v1.0-trainval-part5', verbose=True)

for scene_index in range(1, 800):
    my_scene = nusc.scene[scene_index]
    print(my_scene)
