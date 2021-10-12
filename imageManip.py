import math 
from matplotlib import image, pyplot as plt
import numpy as np
from PIL import Image
import PIL
from skimage import color, io
import skimage
from copy import deepcopy







def load(image_path):
    """Loads an image from a file path.

    HINT: Look up `skimage.io.imread()` function.

    Args:
        image_path: file path to the image.

    Returns:
        out: numpy array of shape(image_height, image_width, 3).
    """
    out = None

    ### YOUR CODE HERE
    # Use skimage io.imread
    out = skimage.io.imread(image_path) # converts image into an array that can be used for analysis
    ### END YOUR CODE
    
    # Let's convert the image to be between the correct range.
    out = out.astype(np.float64) / 255   #The image is brought into the correct range
    return out


def dim_image(image):
    """Change the value of every pixel by following

                        x_n = 0.5*x_p^2

    where x_n is the new value and x_p is the original value.

    Args:
        image: numpy array of shape(image_height, image_width, 3).

    Returns:
        out: numpy array of shape(image_height, image_width, 3).
    """

    out = None

    ### YOUR CODE HERE
    out = 0.5 * image**2   #** is used to represent ^ and it helps to rescale pixel of the image
    ### END YOUR CODE

    return out


def convert_to_grey_scale(image):
    """Change image to gray scale.

    HINT: Look at `skimage.color` library to see if there is a function
    there you can use.

    Args:
        image: numpy array of shape(image_height, image_width, 3).

    Returns:
        out: numpy array of shape(image_height, image_width).
    """
    out = None

    ### YOUR CODE HERE
    out = skimage.color.rgb2gray(image)  #rgb2gray converts the given image to the gray image containing arrays of 0 and 1
    ### END YOUR CODE

    return out


def rgb_exclusion(image_path, channel):
    im = Image.open(image_path).convert('RGB') #opens the image and converts into required format
    r, g, b = im.split()                       #splits image into r,g,and b channels
    if channel == 'R':                         
        r = r.point(lambda i: i * 0)           #r is scaled to 0 hence no red channel
        out = Image.merge('RGB', (r, g, b))    #then remaining channel are merged and image is made with remaining channels
    elif channel == 'G':
        g = g.point(lambda i: i * 0)           #g is scaled to 0
        out = Image.merge('RGB', (r, g, b))     
    elif channel == 'B':
        b = b.point(lambda i: i * 0)           #b is scaled to 0
        out = Image.merge('RGB', (r, g, b))
    return out
    


    """Return image **excluding** the rgb channel specified

    Args:
        image: numpy array of shape(image_height, image_width, 3).
        channel: str specifying the channel. Can be either "R", "G" or "B".

    Returns:
        out: numpy array of shape(image_height, image_width, 3).
    """
\
        

    ### YOUR CODE HERE


   

    ### END YOUR CODE



def lab_decomposition(image, channel):
    """Decomposes the image into LAB and only returns the channel specified.

    Args:
        image: numpy array of shape(image_height, image_width, 3).
        channel: str specifying the channel. Can be either "L", "A" or "B".

    Returns:
        out: numpy array of shape(image_height, image_width).
    """

    lab = color.rgb2lab(image)
    out = None

    ### YOUR CODE HERE
    pass
    ### END YOUR CODE

    return out


def hsv_decomposition(image, channel):
    """Decomposes the image into HSV and only returns the channel specified.

    Args:
        image: numpy array of shape(image_height, image_width, 3).
        channel: str specifying the channel. Can be either "H", "S" or "V".

    Returns:
        out: numpy array of shape(image_height, image_width).
    """

    hsv = color.rgb2hsv(image)   #decomposes image into hsv 
    out = None

    ### YOUR CODE HERE
    if channel == 'H':          
        out = hsv[:, :, 0]       #outputs other channel by setting h to 0
    elif channel == 'S':
        out = hsv[:, :, 1]       # s is set to 0
    elif channel == 'V':
        out = hsv[:, :, 2]       # v is set to 0
    return out
    ### END YOUR CODE

    return out


def mix_images(image1_path, image2_path,  channel1, channel2):
    """Combines image1 and image2 by taking the left half of image1
    and the right half of image2. The final combination also excludes
    channel1 from image1 and channel2 from image2 for each image.

    HINTS: Use `rgb_exclusion()` you implemented earlier as a helper
    function. Also look up `np.concatenate()` to help you combine images.

    Args:
        image1: numpy array of shape(image_height, image_width, 3).
        image2: numpy array of shape(image_height, image_width, 3).
        channel1: str specifying channel used for image1.
        channel2: str specifying channel used for image2.

    Returns:
        out: numpy array of shape(image_height, image_width, 3).
    """

    out = None
    ### YOUR CODE HERE
    out1 = rgb_exclusion(image1_path, channel1) #function is used from above to remove one channel and merge other channels
    out2 = rgb_exclusion(image2_path, channel2)
    out = np.concatenate((out1, out2), axis = 1 ) #np.concatenate to mix two images together
    ### END YOUR CODE

    return out


def mix_quadrants(image):
    """THIS IS AN EXTRA CREDIT FUNCTION.

    This function takes an image, and performs a different operation
    to each of the 4 quadrants of the image. Then it combines the 4
    quadrants back together.

    Here are the 4 operations you should perform on the 4 quadrants:
        Top left quadrant: Remove the 'R' channel using `rgb_exclusion()`.
        Top right quadrant: Dim the quadrant using `dim_image()`.
        Bottom left quadrant: Brighthen the quadrant using the function:
            x_n = x_p^0.5
        Bottom right quadrant: Remove the 'R' channel using `rgb_exclusion()`.

    Args:
        image1: numpy array of shape(image_height, image_width, 3).

    Returns:
        out: numpy array of shape(image_height, image_width, 3).
    """
    out = None

    ### YOUR CODE HERE
    pass
    ### END YOUR CODE

    return out
