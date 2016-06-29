#!/usr/bin/env python
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

imageNumberFour = 'images/numbers/y0.4.png'
image_dotndot = 'images/dotndot.png'

currentImage = Image.open(imageNumberFour)

imageArray = np.asarray(currentImage)

print(imageArray)

# Display the image
plt.imshow(imageArray)
print(imageArray)
plt.show()
