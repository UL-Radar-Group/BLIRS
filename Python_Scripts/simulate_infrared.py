import bpy

# The bend File to be rendered
blendfilepath = '/home/johann/Work/Masters_Project/blirs/Blend_File/scene.blend'
# open the blend File
bpy.ops.wm.open_mainfile(filepath=blendfilepath)

#Set the Camera Focallength
camerafocallen = 16
camerawidth = 32
objects = bpy.context.scene.objects
for ob in objects:
    if ob.type == 'CAMERA':
        ob.data.lens = camerafocallen
        ob.data.sensor_width = camerawidth
    else: pass


# switch to Infrared Scene Settings
bpy.ops.object.change_materials(change_to_radar = False, change_to_ir = True)
scene = bpy.context.scene

# The resolution of the output
ir_resolution_x = 500
ir_resolution_y = 500
scene.render.resolution_x = ir_resolution_x
scene.render.resolution_y = ir_resolution_y
scene.render.resolution_percentage = 100


# Number of Frames
numofFrames = 2
#scene.frame_end = numofFrames
# Frame Rate per Second
fps = 1

# Render the output in HDR format
scene.render.image_settings.file_format = 'HDR'

# Output File Path
outputfile = '/home/johann/Work/Masters_Project/blirs/Infrared_Renders/'
# Name of the Output Files
filename = 'scene_ir_test'
scene.render.filepath = outputfile + filename

#Set the Camera Focallength
camerafocallen = 16
# Set theCamera Width
camerawidth = 32
objects = bpy.context.scene.objects
for ob in objects:
    if ob.type == 'CAMERA':
        ob.data.lens = camerafocallen
        ob.data.sensor_width = camerawidth
    else: pass



scene.use_nodes = False
bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = numofFrames  
bpy.context.scene.render.fps = fps

# Export the camera patj
objects = bpy.context.scene.objects
for ob in objects:
    if ob.type == 'CAMERA':
        ob.select = True
    else: pass
bpy.ops.export_animation.cameras(filepath = outputfile + 'Camerapath.py',frame_start=1,frame_end=numofFrames)
# Use SKy
bpy.context.scene.render.layers["RenderLayer"].use_sky = True
# Render the animation
bpy.ops.render.render(animation = True)

