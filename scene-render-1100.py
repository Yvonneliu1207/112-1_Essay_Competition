from nuscenes.nuscenes import NuScenes
import os

nusc = NuScenes(version='v1.0-trainval', dataroot='/Users/yvonne/work/nuscenes-devkit/v1.0-trainval-part10', verbose=True)

my_scene_token = nusc.field2token('scene', 'name', 'scene-1100')[0]


nusc.render_scene_channel(my_scene_token, 'CAM_FRONT', 
                          freq=30, imsize=(1280,720), 
                          out_path=os.path.expanduser('~/work/scene-1100_CAM_FRONT.avi'))

# # nuscenes-lidarseg
nusc.render_scene_channel_lidarseg(my_scene_token,
                                   'CAM_FRONT',
                                   filter_lidarseg_labels=[2,3,4,5,6,7,8,14,15,16,17,18,19,20,21,22,23],
                                   verbose=True,
                                   dpi=100,
                                   imsize=(1280, 720),
                                   render_mode='video',
                                   out_folder=os.path.expanduser('~/work/lidarseg'))
