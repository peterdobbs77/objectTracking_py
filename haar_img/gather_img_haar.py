import urllib.request
import cv2.cv2 as cv2
import numpy as numpy
import os


def store_raw_images():
    # negative images are from the sports,atheletics page of ImageNet
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00468480'
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()

    if not os.path.exists('neg'):
        os.makedirs('neg')

    for pic_num, url in enumerate(neg_image_urls.split('\n')):
        try:
            print(url)
            urllib.request.urlretrieve(url, 'neg/'+str(pic_num)+'.jpg')
            img = cv2.imread('neg/'+str(pic_num)+'.jpg', cv2.IMREAD_GRAYSCALE)
            resized_img = cv2.resize(img, (100, 100))
            cv2.imwrite('neg/'+str(pic_num)+'.jpg', resized_img)

        except Exception as e:
            print(str(e))


store_raw_images()
