from PIL import Image
from PIL import ImageDraw

def numToBinary(N):
    if N < 2:
        #if N is 0 or 1 then it returns N
        return str(N)
    else:
        #if N is not 0 or 1 it continues until it breaks N down to a 0 or 1
        return str(numToBinary(N/2))+ str(N%2)

def mostSignificant2(num):
    return num >> 6

def mostSignificantN(num, N):
    return num >> (8-N)

bear = Image.open("stoneteddybear.jpg")
blue = Image.open("blue.jpg")

def shift2BitsTo8(num):
    if num < 0 or num > 3:
        return "That is an invalid number!"
    return num << 6

def degradeColors2Bits(pic):
    picCopy = Image.new('RGB', pic.size, (0, 0, 0))
    for x in range(pic.size[0]):
        for y in range(pic.size[1]):
          (r,g,b) = pic.getpixel((x, y))
          r = mostSignificant2(r)
          g = mostSignificant2(g)
          b = mostSignificant2(b)
          r2 = shift2BitsTo8(r)
          g2 = shift2BitsTo8(g)
          b2 = shift2BitsTo8(b)
          picCopy.putpixel((x,y), (r2,g2,b2))
    picCopy.show()


def shiftNBitsTo8(num, N):
    return num << (8-N)

def degradeColorsNBits(pic, N):
    picCopy = Image.new('RGB', pic.size, (0, 0, 0))
    for x in range(pic.size[0]):
        for y in range(pic.size[1]):
          (r,g,b) = pic.getpixel((x, y))
          r = mostSignificantN(r, N)
          g = mostSignificantN(g, N)
          b = mostSignificantN(b, N)
          r2 = shiftNBitsTo8(r, N)
          g2 = shiftNBitsTo8(g, N)
          b2 = shiftNBitsTo8(b, N)
          picCopy.putpixel((x,y), (r2,g2,b2))
    picCopy.show()

#Writing the Code... Top-down Design
def embedDigits2(contextVal, messageVal):
    if contextVal < 0 or contextVal > 255:
        return "That is an invalid number!"
    if messageVal < 0 or messageVal > 3:
        return "That is an invalid number!"
    contextVal = (contextVal >> 2) << 2
    return contextVal|messageVal

######################TO DO##########################
def embedDigitsN(contextVal, messageVal, N):
    if N != len(numToBinary(messageVal)):
        messageVal = (messageVal << (8-len(numToBinary(messageVal)))) >> (8-N)
    contextVal = (contextVal >> N) << N
    return contextVal | messageVal

def getLeastSignificant2(num):
    return num%4

def getLeastSignificantN(num, N):
    return num%(2**(N))

bear = Image.open("stoneteddybear.jpg")
blue = Image.open("blue.jpg")

#Putting it all Together
def hideSecretMessage2Bits(context, message):
    contextWidth = context.size[0]
    contextHeight = context.size[1]

    messageWidth = message.size[0]
    messageHeight = message.size[1]
    
    leastWidth = messageWidth
    leastHeight = messageHeight
    
    if messageWidth > contextWidth:
        leastWidth = contextWidth
    if messageHeight > contextHeight:
        leastHeight = contextHeight   

    contextOutput = Image.new('RGB', (contextWidth, contextHeight), "white")    
          
          
    for xCon in range(contextWidth):
        for yCon in range(contextHeight):
            (rC, gC, bC) = context.getpixel((xCon,yCon))
            rC = (rC >> 2) << 2
            gC = (gC >> 2) << 2
            bC = (bC >> 2) << 2
            contextOutput.putpixel((xCon,yCon), (rC,gC,bC))

    for xMes in range(leastWidth):
        for yMes in range(leastHeight):
            (rM,gM,bM) = message.getpixel((xMes, yMes))
            rM = rM >> 6
            gM = gM >> 6
            bM = bM >> 6
          
            (rC, gC, bC) = contextOutput.getpixel((xMes,yMes))
            rNew = rM|rC
            gNew = gM|gC
            bNew = bM|bC
            contextOutput.putpixel((xMes,yMes), (rNew,gNew,bNew))
    contextOutput.show()
    contextOutput.save("stoneteddybearwith.bmp")
    
def recoverSecretMessage2Bits(context):
    context = Image.open(context)
    contextWidth = context.size[0]
    contextHeight = context.size[1]
    
    message = Image.new("RGB", (contextWidth,contextHeight), "white")

    for xCon in range(contextWidth):
        for yCon in range(contextHeight):
            (rC,gC,bC) = context.getpixel((xCon,yCon))
            rC = (rC & 3) << 6
            gC = (gC & 3) << 6
            bC = (bC & 3) << 6
            message.putpixel((xCon,yCon), (rC,gC,bC))
    message.show()

def hideSecretMessageNBits(context, message, N):
    contextWidth = context.size[0]
    contextHeight = context.size[1]

    messageWidth = message.size[0]
    messageHeight = message.size[1]
    
    leastWidth = messageWidth
    leastHeight = messageHeight
    
    if messageWidth > contextWidth:
        leastWidth = contextWidth
    if messageHeight > contextHeight:
        leastHeight = contextHeight   

    contextOutput = Image.new('RGB', (contextWidth, contextHeight), "white")    
          
          
    for xCon in range(contextWidth):
        for yCon in range(contextHeight):
            (rC, gC, bC) = context.getpixel((xCon,yCon))
            rC = (rC >> N) << N
            gC = (gC >> N) << N
            bC = (bC >> N) << N
            contextOutput.putpixel((xCon,yCon), (rC,gC,bC))

    for xMes in range(leastWidth):
        for yMes in range(leastHeight):
            (rM,gM,bM) = message.getpixel((xMes, yMes))
            rM = rM >> (8-N)
            gM = gM >> (8-N)
            bM = bM >> (8-N)
          
            (rC, gC, bC) = contextOutput.getpixel((xMes,yMes))
            rNew = rM|rC
            gNew = gM|gC
            bNew = bM|bC
            contextOutput.putpixel((xMes,yMes), (rNew,gNew,bNew))
    contextOutput.show()
    #contextOutput.save("stoneteddybearwith.bmp")

def recoverSecretMessageNBits(context, N):
    context = Image.open(context)
    contextWidth = context.size[0]
    contextHeight = context.size[1]
    
    message = Image.new("RGB", (contextWidth,contextHeight), "white")

    for xCon in range(contextWidth):
        for yCon in range(contextHeight):
            (rC,gC,bC) = context.getpixel((xCon,yCon))
            rC = (rC & (2**N - 1)) << (8-N)
            gC = (gC & (2**N - 1)) << (8-N)
            bC = (bC & (2**N - 1)) << (8-N)
            message.putpixel((xCon,yCon), (rC,gC,bC))
    message.show()
