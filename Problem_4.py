def sepia(oldPixel):
    red = oldPixel.getRed()
    green = oldPixel.getGreen()
    blue = oldPixel.getBlue()
    newRed = int(red * 0.393 + green * 0.769 + blue * 0.189)
    newGreen = int(red * 0.349 + green * 0.686 + blue * 0.168)
    newBlue = int(red * 0.272 + green * 0.534 + blue * 0.131)
    newPixel = Pixel(newRed, newGreen, newBlue)
    return newPixel

def generalScale(oldimage, widthscale, heightscale):
    oldw = oldimage.getWidth()
    oldh = oldimage.getHeight()
    newim = EmptyImage(oldw * witdhscale, oldh * heightscale)

    for row in range(newim.getHeight()):
        for col in range(newim.getWidth()):
            originalCol = col//widthscale
            orignalRow = row//heightscale
            oldpixel = oldimage.getPixel(originalCol, originalRow)
            newim.setPixel(col, row, oldpixel)

    return newim

def originalScale(oldimage):
    for now in range(oldimage.getHeight()):
        for col in range(oldimage.getWidth()):
            oldpixel = oldimage.getPixel(col, row)
            sepieImage = sepia(oldpixel)
            oldimage.setPixel(col, row, sepieImage)

    return oldimage

def displayImage(Image):
    empWin = ImageWin("Image Processing", Image.getWidth(), Image.getHeight())
    Image.draw(empWin)

img = Image('deadpool.jpg')
sepia = originalScale(img)
new = generalScale(sepia, 1, 2)
displayImage(new)
            
