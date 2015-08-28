from PIL import Image
from PIL import ImageDraw
from random import*

im = Image.open("stoneteddybear.jpg")

imsize = im.size
width = imsize[0]
height = imsize[1]


def greyscale(im):
    draw = ImageDraw.Draw(im)
    width, height = im.size
    for x in range(width):
        for y in range(height):
            (red, green, blue) = im.getpixel((x,y))
            newRed = red*0.21
            newGreen = green*0.72
            newBlue = blue*0.07
            luminance = newRed + newGreen + newBlue
            luminance = int(luminance)
            draw.point([(x,y)], (luminance, luminance, luminance))
    im.show()

def binarize(im, threshold):
    draw = ImageDraw.Draw(im)

    for x in range(width):
        for y in range(height):
            (red, green, blue) = im.getpixel((x,y))
            newRed = red*0.21
            newGreen = green*0.72
            newBlue = blue*0.07
            avgRGB = newRed + newGreen + newBlue
            avgRGB = int(avgRGB)
            if avgRGB > threshold:
                draw.point([(x,y)], (255, 255, 255))
            else:
                draw.point([(x,y)], (0, 0, 0))
    im.show()

def mirrorVert(im):
    draw = ImageDraw.Draw(im)

    for x in range(width):
        for y in range(0, height/2):
            (red, green, blue) = im.getpixel((x,y))
            draw.point([(x,height-1 - y)], (red, green, blue))
    im.show()

def flipHoriz(im):
    draw = ImageDraw.Draw(im)

    for x in range(0, width/3):
        for y in range(height):
            (red, green, blue) = im.getpixel((x,y))
            (flipRed, flipGreen, flipBlue) = im.getpixel((width-1 - x, y))
            draw.point([(width-1 - x,y)], (red, green, blue))
            draw.point([(x,y)], (flipRed, flipGreen, flipBlue))
    im.show()

def scale(im):
    draw = ImageDraw.Draw(im)
    im2 = Image.new("RGB", (width/2, height/2), "white")
    drawScale = ImageDraw.Draw(im2)

    for x in range(0, width, 2):
        for y in range(0, height, 2):
            (red, green, blue) = im.getpixel((x,y))
            drawScale.point([(x/2,y/2)], (red, green, blue))
    im2.show()

def blur(im):
    draw = ImageDraw.Draw(im)
    im2 = Image.new("RGB", (width, height), "white")
    drawIm2 = ImageDraw.Draw(im2)

    for x in range(0, width+2, 3):
        for y in range(0, height+2, 3):
            (red, green, blue) = im.getpixel((x,y))
            (red1, green1, blue1) = im.getpixel((x,y+1))
            (red2, green2, blue2) = im.getpixel((x,y+2))
            (red3, green3, blue3) = im.getpixel((x+1,y))
            (red4, green4, blue4) = im.getpixel((x+1,y+1))
            (red5, green5, blue5) = im.getpixel((x+1,y))
            (red6, green6, blue6) = im.getpixel((x+2,y))
            (red7, green7, blue7) = im.getpixel((x+2,y+1))
            (red8, green8, blue8) = im.getpixel((x+2,y))

            avgRed = (red + red1 + red2 + red3 + red4 + red5 + red6 + red7 + red8)/9
            avgGreen = (green + green1 + green2 + green3 + green4 + green5 + green6 + green7 + green8)/9
            avgBlue = (blue + blue1 + blue2 + blue3 + blue4 + blue5 + blue6 + blue7 + blue8)/9

            drawIm2.point([(x,y)], (avgRed, avgGreen, avgBlue))
            drawIm2.point([(x, y+1)], (avgRed, avgGreen, avgBlue))
            drawIm2.point([(x, y+2)], (avgRed, avgGreen, avgBlue))
            drawIm2.point([(x+1, y)], (avgRed, avgGreen, avgBlue))
            drawIm2.point([(x+1, y+1)], (avgRed, avgGreen, avgBlue))
            drawIm2.point([(x+1, y+2)], (avgRed, avgGreen, avgBlue))
            drawIm2.point([(x+2, y)], (avgRed, avgGreen, avgBlue))
            drawIm2.point([(x+2, y+1)], (avgRed, avgGreen, avgBlue))
            drawIm2.point([(x+2, y+2)], (avgRed, avgGreen, avgBlue))
    im2.show()

##def randomGrid(im, n):
##    draw = ImageDraw.Draw(im)
##    im2 = Image.new("RGB", (width, height), "white")
##    drawIm2 = ImageDraw.Draw(im2)
##
##    liststartpt[]
##    liststartptrand[]
##
##    for x in range(0,n):
##        for y in range(0,n):
##            liststartpt.append([width*x/n, height*y/n])
##            
##            (red, green, blue) = im.getpixel((x, y))
