import numpy as np
import skimage
import matplotlib.pyplot as plt

#Part-1
#Loading image data into a nd-array
data = skimage.io.imread('scenery.jpeg')

#Part-2
#Printing no of pixels of given image
pixels = data.size
print(pixels)

#Part-4
#Converting into Grey-Scale
imG = skimage.color.rgb2gray(data)
#skimage.io.imsave("GreyScaleScenery.png", imG)

#Horizontal flipping
horizontal_flip = data[:, ::-1]
#skimage.io.imsave("HorizontalFlip.png", horizontal_flip)

#Vertical flipping
vertical_flip = data[::-1, :]
#skimage.io.imsave("VerticalFlip.png", vertical_flip)

#Means
mean_original = data.mean()
print(mean_original)
mean_GreyScale = imG.mean()
print(mean_GreyScale)

#Subplots for image and GreyScale image
plt.subplot(121)
plt.imshow(data)
plt.subplot(122)
plt.imshow(imG)
#plt.show()

#Subplots for image and Horizontally flipped image
plt.subplot(121)
plt.imshow(data)
plt.subplot(122)
plt.imshow(horizontal_flip)
#plt.show()

#Subplots for image and Vertically flipped image
plt.subplot(121)
plt.imshow(data)
plt.subplot(122)
plt.imshow(vertical_flip)
#plt.show()

red = data[:, :, 0] 
#skimage.io.imsave("Red.png", red)
#print(np.amax(red))

green = data[:, :, 1]
#skimage.io.imsave("Green.png", green)
#print(np.amax(green))

blue = data[:, :, 2]
#skimage.io.imsave("Blue.png", blue)
#print(np.amax(blue))
