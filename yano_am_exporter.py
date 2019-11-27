import bpy
import os
import os.path
import json

def write_file( fname, content ):
    with open(fname, 'w', encoding='utf-8') as f:
      json.dump(content, f, ensure_ascii=False, indent=4)

def ensure_folder_exist( foldername ):
    if not os.access( foldername, os.R_OK|os.W_OK|os.X_OK ):
        os.makedirs( foldername )

def ensure_extension( filepath, extension ):
    if not filepath.lower().endswith( extension ):
        filepath += extension
    return filepath

def frame_to_time(frame_number, fps):
    raw_time = (frame_number - 1) / fps
    return round(raw_time, 3)

def save(operator, context, filepath=""):
  filepath = ensure_extension( filepath, ".json")

  # The current scene data.
  scene = bpy.context.scene
  fps = scene.render.fps
  fps_base = scene.render.fps_base

  # Markers
  # https://docs.blender.org/api/current/bpy.types.Scene.html#bpy.types.Scene.timeline_markers
  markers = scene.timeline_markers
  jsonData = {}
  jsonData['markers'] = []
  for k, v in scene.timeline_markers.items():
    frame = v.frame
    frame_time = frame_to_time(frame, fps)
    jsonData['markers'].append({
        'name': v.name,
        'time': frame_time,
        'frame': frame
    })

  write_file( filepath, jsonData )
  return {"FINISHED"}