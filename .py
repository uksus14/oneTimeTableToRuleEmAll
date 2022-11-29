from PIL import Image, ImageDraw
from random import randint
c = lambda:(randint(0, 255), randint(0, 255), randint(0, 255))
png = Image.open(r"C:\Users\akylo\Desktop\Pr\first_tiktok\barsbek.png")
shadow = ImageDraw.Draw(png)
width = png.size[0]
height = png.size[1]
pix = png.load()
for y in range(height):
    for x in range(width):
        if pix[x, y][3]:
            color = 255
        else:
            color = 0
        shadow.point((x, y), (0, 0, 0, color))

png.save(r"C:\Users\akylo\Desktop\Pr\first_tiktok\barsbek_shadow.png", "PNG")