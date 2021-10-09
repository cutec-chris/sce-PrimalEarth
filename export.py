import sys,pathlib;sys.path.append(str(pathlib.Path(__file__).parent.parent))
from blender_export import *
ExportObject('Plants/Air/Air.blend','airplant.stl.cleaner.materialmerger.gles','plant_air.glb')