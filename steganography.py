from PIL import Image
import stepic

im = Image.open('image.png')
message = stepic.decode(im)
print('message: {}'.format(message))
