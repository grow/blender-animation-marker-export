bl_info = {
    "name" : "yano-am-export",
    "author" : "Scott Yano",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location": "File > Import-Export",
    "warning" : "",
    "category" : "Generic"
}

import bpy
from bpy.props import *
from bpy_extras.io_utils import ExportHelper


class ExportJSON( bpy.types.Operator, ExportHelper ):
    bl_idname = "export.json"
    bl_label = "Export JSON"

    filename_ext = ".json"

    def invoke( self, context, event ):
        return ExportHelper.invoke( self, context, event )

    @classmethod
    def poll( cls, context ):
        return context.active_object != None

    def execute( self, context ):
        print("Selected: " + context.active_object.name )

        if not self.properties.filepath:
            raise Exception("filename not set")

        filepath = self.filepath

        from . yano_am_exporter import save
        return save( self, context, **self.properties )


def export_menu( self, context ):
    default_path = bpy.data.filepath.replace(".blend", ".json")
    self.layout.operator( ExportJSON.bl_idname, text="Animation Marker Export").filepath = default_path

def register():
    bpy.utils.register_class(ExportJSON)
    bpy.types.TOPBAR_MT_file_export.append(export_menu)

def unregister():
    bpy.utils.unregister_class(ExportJSON)
    bpy.types.TOPBAR_MT_file_export.remove(export_menu)



if __name__ == "__main__":
    register()