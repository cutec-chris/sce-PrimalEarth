import sys,pathlib;sys.path.append(str(pathlib.Path(__file__).parent.parent))
from blender_export import *
ExportObject('Plants/Prayer/Prayer.blend','Prayer','Plants/Prayer/prayer',export_image_format='JPEG')