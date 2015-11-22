# import the necessary packages
from skimage.measure import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2

def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
                            
    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err
                                     
def compare_images(imageA, imageB, title):
    # compute the mean squared error and structural similarity
    # index for the images
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)
                                                         
    # setup the figure
    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
                                                                     
    # show first image
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA)
    plt.axis("off")
                                                                                     
    # show the second image
    ax = fig.add_subplot(1, 2, 2)   
    plt.imshow(imageB)
    plt.axis("off")
                                                                                                     
    # show the images
    plt.show()


# load the images -- the original, the original + contrast,
# and the original + photoshop
original = cv2.imread("xsampel-a.png")
contrast = cv2.imread("xsampel-b.png")
  
# convert the images to grayscale
# initialize the figure
fig = plt.figure("Images")
images = ("Original", original), ("Contrast", contrast)
 
# loop over the images
for (i, (name, image)) in enumerate(images):
    # show the image
    ax = fig.add_subplot(1, 3, i + 1)
    ax.set_title(name)
    plt.imshow(images)
    plt.axis("off")
                         
    # show the figure
    plt.show()
                          
    # compare the images
    compare_images(original, contrast, "Sampel A vs. Sampel B")
    
