from PIL import Image, ImageFilter

before = Image.open("")
after = before.filter(ImageFilter.BoxBlur(10))
after.save("out.bmp")

