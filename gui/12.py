from PIL import Image,ImageFilter
import os
image1=Image.open('download.jpg')
# image1.rotate(90).save('abcd.jpg')
# image1.convert(mode='L').save('black.jpg')
# image1.convert(mode='L').rotate(90).save('123.jpg')
# image1.filter(ImageFilter.GaussianBlur(15)).save('234.jpg')
# image1.convert(mode='1').save('1.jpg')
#image1.convert(mode='P').save('2.jpg')
#image1.convert(mode='RGB').save('3.jpg')
#image1.convert(mode='RGBA').save('4.jpg')
#image1.convert(mode='CMYK').save('5.jpg')
#image1.convert(mode='YCbCr').save('6.jpg')
#image1.convert(mode='I').save('7.jpg')
image1.show()
print("image save successfully")
#HSV,LAB,F