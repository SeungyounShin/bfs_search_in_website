from keras import backend
from keras.preprocessing.image import img_to_array,load_img
import tensorflow as tf
from keras import backend as K
import numpy as np
import os
import math

path = '/Users/seungyoun/Desktop/ImageFinder/pic'

def loss(a,b):
    return np.sqrt(np.sum(np.square(a-b)))

def img_resize(img,height,width):
  shape = img.shape
  ordirany_img_shape = shape
  img = img.reshape((1,) + shape)
  x = tf.image.resize_images(
      img,
      [height,width],
      method=tf.image.ResizeMethod.BILINEAR,
      align_corners=False
  )
  y = tf.Session().run(x)
  return y

category = []
for i in os.listdir(path):
    if(i=='.DS_Store'):
        continue
    category.append(path + '/' + str(i))


class Test:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.sum_of_result = 0
        self.div = 0

    def test(self):
        sum_of_result = 0
        div = 0
        print("START : ",category[self.a],category[self.b])
        cnt1 = 0
        cnt2 = 0
        test1 = [category[self.a]+'/'+str(i) for i in os.listdir(category[self.a])]
        test2 = [category[self.b]+'/'+str(i) for i in os.listdir(category[self.b])]
        max1 = 0
        max2=0
        for i in test1:
            cnt1 += 1
            cnt2 = 0
            for j in test2:
                cnt2 += 1
                img1 = load_img(i)
                img2 = load_img(j)
                img1 = img_to_array(img1)
                img2 = img_to_array(img2)
                shape1 = img1.shape
                shape2 = img2.shape
                resize_shape = min(shape1,shape2)
                img1 = img_resize(img1,resize_shape[1],resize_shape[2])
                img2 = img_resize(img2,resize_shape[1],resize_shape[2])
                result = loss(img1,img2)
                #print(cnt1," and ",cnt2," : ",result)
                self.sum_of_result += result
                max1 = max(cnt1,max1)
                max2 =max(cnt2,max2)
        self.div =max1*max2
        print(self.a,self.b,"DONE")
    def average(self):
        try:
            return self.sum_of_result/self.div
        except:
            print("sum of result is ",self.sum_of_result)


avg = [[]]
for i in range(0,3):
    for j in range(0,3):
        test = Test(i,j)
        test.test()
        print(i,j,test.average())

print(avg)
