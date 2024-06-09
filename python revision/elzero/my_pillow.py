from PIL import Image

# open the image
my_img = Image.open(r'Z:\UNI\study\python for AI\photos\fork.jpeg')

my_img.show()

myBox = (300, 300, 800, 800) # (left, upper, right, lower)