import os.path as osp
import json
class DatasetProvider:
  def __init__(self,root, transforms_file,half_resolution=True):
    self.mata = json.load(open(osp.join(root,transforms_file)))
    self.root = root
    self.frames = self.mata["frames"]
    self.images = []
    self.poses = []
    self.camera_angle_x = self.mata["camera_angle_x"]


root = "lego"
transformes_file = "transforms_test.json"
half_resolution = False
provider = DatasetProvider(root ,transformes_file)
