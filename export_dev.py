import sys,pathlib;sys.path.append(str(pathlib.Path(__file__).parent.parent))
from blender_export import *
ExportObject('Dinos/Dimorphodon/Dimorphodon.blend','Dimorphodon','Dinos/Dimorphodon/dimorphodon',lod=[10],export_image_format='JPEG')