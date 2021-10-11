import sys,pathlib;sys.path.append(str(pathlib.Path(__file__).parent.parent))
from blender_export import *
ExportObject('Plants/Prayer/Prayer.blend','Prayer','Plants/Prayer/prayer',lod_ligthing=1000,export_image_format='JPEG')
#ExportObject('Plants/Palm/Palms.blend','Collection 1','Plants/Palm/palm01',export_image_format='AUTO')
ExportObject('Plants/Tropic1/trop_leav 4.blend','Collection 1','Plants/Tropic1/tropic1')
ExportObject('Plants/Tropic2/Tropic2.blend','Collection','Plants/Tropic2/tropic2',lod_ligthing=1500)
ExportObject('Plants/Tropic3/Tropic3.blend','Collection','Plants/Tropic3/tropic3')
ExportObject('Plants/Tropic4/Tropic4.blend','Collection','Plants/Tropic4/tropic4')
