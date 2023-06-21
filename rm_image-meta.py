from PIL import Image

original_img = Image.open('sunset.jpeg')
data = list(original_img.getdata()) # copies image without metadata
new_img = Image.new(original_img.mode, original_img.size)
new_img.putdata(data)
new_img.save('sunset2.jpeg')
new_img.close()