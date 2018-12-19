import gphoto2 as gp
context = gp.Context()
camera = gp.Camera()
camera.init(context)
text = camera.get_config(context)
print('Summary')
print('=======')
print(str(text))
camera.exit(context)
