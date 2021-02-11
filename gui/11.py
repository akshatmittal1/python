from PIL import Image,ImageFilter
import os
size_300=(118,200)
#os.chdir("")
for f in os.listdir():
    if f.endswith('.jpg'):
        i=Image.open(f)
        print(f)
        fn,text=os.path.splitext(f)
        i.thumbnail(size_300,Image.ANTIALIAS)
        i.save('abc/{}.png'.format(fn))
print("file extension change")
