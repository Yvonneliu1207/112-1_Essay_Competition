from nuscenes.nuscenes import NuScenes
import cv2
import os

nusc = NuScenes(version='v1.0-trainval', dataroot='/Users/samuel/work/nuscenes-devkit/v1.0-trainval-part10', verbose=True)

my_scene_token = nusc.field2token('scene', 'name', 'scene-1100')[0]

# Get records from DB.
scene_rec = nusc.get('scene', my_scene_token)
sample_rec = nusc.get('sample', scene_rec['first_sample_token'])
sd_rec = nusc.get('sample_data', sample_rec['data']['CAM_FRONT'])

imsize=(1280,720)

#if out_path is not None:
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('./scene-1100_CAM_FRONT_raw_image.avi', fourcc, 30, (1280,720))
#else:
#    out = None

has_more_frames = True
while has_more_frames:

    # Get data from DB.
    impath, boxes, camera_intrinsic = nusc.get_sample_data(sd_rec['token'])
                                         # box_vis_level=BoxVisibility.ANY)

    # Load and render.
    #if not osp.exists(impath):
    #    raise Exception('Error: Missing image %s' % impath)
    im = cv2.imread(impath)
    #samuel
    #for box in boxes:
    #    c = self.get_color(box.name)
    #    box.render_cv2(im, view=camera_intrinsic, normalize=True, colors=(c, c, c))

    # Render.
    im = cv2.resize(im, imsize)
    #cv2.imshow(name, im)
    #if out_path is not None:
    out.write(im)

    key = cv2.waitKey(10)  # Images stored at approx 10 Hz, so wait 10 ms.

    if not sd_rec['next'] == "":
        sd_rec = nusc.get('sample_data', sd_rec['next'])
    else:
        has_more_frames = False




