from PIL import Image
import stepic

im = Image.open('discoimage.png')
message = stepic.decode(im)
print('message: {}'.format(message))