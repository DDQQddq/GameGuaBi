from PIL import Image
from PIL import EpsImagePlugin

EpsImagePlugin.gs_windows_binary = r'C:\Program Files\gs\gs9.55.0\bin\gswin64c'
im = Image.open('BingDwenDwen.eps')
im.save('BingDwenDwen.jpg', 'JPEG')
