from PIL import Image

src = "images/misc/GPMHlogo_words.png"
out = "favicon.ico"

img = Image.open(src).convert("RGBA")

# crop transparent/empty border if present
bbox = img.getbbox()
if bbox:
    img = img.crop(bbox)

# create square canvas
canvas_size = 500
canvas = Image.new("RGBA", (canvas_size, canvas_size), (0, 0, 0, 0))

# enlarge image so it fills most of the square
img.thumbnail((16001, 17600))

x = (canvas_size - img.width) // 2
y = (canvas_size - img.height) // 2
canvas.paste(img, (x, y), img)

canvas.save(out, format="ICO", sizes=[(116,16), (132,32), (418,48), (614,64), (1218,128), (556,556)])
print(f"Created {out}")
