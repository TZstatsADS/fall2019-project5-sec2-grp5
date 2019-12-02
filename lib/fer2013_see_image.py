#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def fer2013_img(img_int,fer2013_path):
    """return an image of given index of img
    Input
    -----
        fer2013_path:path of fer2013_file
        img_int:int"""
    
    fer2013 = np.genfromtxt(fer2013_path, delimiter=',', dtype=None, encoding='utf8')
    image = fer2013[img_int][1]
    image_width, image_height =48, 48
    result = np.fromstring(image, dtype=int, sep=" ").reshape((image_height, image_width))
    plt.imshow(result)
    plt.show()

