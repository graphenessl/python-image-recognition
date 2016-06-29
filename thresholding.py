#!/usr/bin/env python

# Python image thresholding
# 05.06.2016

from PIL import Image
import numpy as np

import matplotlib.pyplot as plt
import time

# Function: Thresholding:
# The idea of thresholding is to make images "clearer" by turning each pixel
# to a maximum. If it's a darker pixel, it will be rendered as black, if it's
# ligther, then it will be rendered as white
# Now what we want to do is create a function that will take the images we feed
# it, and threshold it. The way we're going to do this is by taking the
# "average" color value, and then thresholding any pixel as black if it is any
# darker or white if it is lighter.
# What we've added for now is, from the average of the balance array, we then assess each pixel. If the pixel is brighter than the average, then it is a white. If it is darker than the average, then it is black.
# Now, what we can do with this function is feed in the image array, and we're
# going to be returned the thresholded image array.
def threshold(imageArray):
    balanceAr = []
    newAr = imageArray

    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = reduce(lambda x, y: x + y, eachPix[:3]) / len(eachPix[:3])
            balanceAr.append(avgNum)

    balance = reduce(lambda x, y: x + y, balanceAr) / len(balanceAr)

    for eachRow in newAr:
        for eachPix in eachRow:
            if reduce(lambda x, y: x + y, eachPix[:3]) / len(eachPix[:3]) > balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                eachPix[3] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                eachPix[3] = 255
    return newAr

i = Image.open('images/numbers/0.1.png')
iar = np.array(i)
i2 = Image.open('images/numbers/y0.4.png')
iar2 = np.array(i2)
i3 = Image.open('images/numbers/y0.5.png')
iar3 = np.array(i3)
i4 = Image.open('images/sentdex.png')
iar4 = np.array(i4)


iar = threshold(iar)
iar2 = threshold(iar2)
iar3 = threshold(iar3)
iar4 = threshold(iar4)

fig = plt.figure()
ax1 = plt.subplot2grid((8,6),(0,0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8,6),(4,0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8,6),(0,3), rowspan=4, colspan=3)
ax4 = plt.subplot2grid((8,6),(4,3), rowspan=4, colspan=3)

ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)


plt.show()
