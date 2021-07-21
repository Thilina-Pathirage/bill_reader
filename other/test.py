import easyocr
from pylab import rcParams
from PIL import Image
from PIL import ImageDraw
rcParams['figure.figsize'] = 8,16

reader = easyocr.Reader(['en'], gpu=False)

image=Image.open("../images/invoice.png")

output = reader.readtext('/Image1.jpg')
bound = reader.readtext(image)
img = Image.open('/Image1.jpg')
def draw_boxes(image, bound, color='yellow', width=2):
  draw = ImageDraw.Draw(image)
  for bounds in bound:
    p0, p1, p2, p3 = bounds[0]
    draw.line([*p0, *p1, *p2, *p3], fill=color, width=width)
  return image

draw_boxes(img, bound)


text=''
for i in range(len(bound)):
  text = text + bound[i][1]+'\n'

print(text)

