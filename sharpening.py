#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# + {}
# # !pip install opencv-python==3.4.9.33
# -

import cv2
import numpy as np

sobel_gradient_y_mask = np.array(
   [[-1, 0, 1], 
    [-2, 0, 2], 
    [-1, 0, 1]])
sobel_gradient_x_mask = np.array(
   [[-1, -2, -1],
    [ 0,  0,  0], 
    [ 1,  2,  1]])
laplacian_mask = np.array(
   [[-1, -1, -1],
    [-1,  8, -1], 
    [-1, -1, -1]])
average_mask = np.array(
   [[0.11111111, 0.11111111, 0.11111111],
    [0.11111111, 0.11111111, 0.11111111],
    [0.11111111, 0.11111111, 0.11111111]])   # 0.1111111 means 1/9

img_file = 'flower_1'
# img_file = 'bird_4_corp'
# img_file = '20070401_121'
# img_file = 'IMG_7367_2'
pic = cv2.imread("images/" + img_file+'.jpg')
print(pic.shape)
# print(pic.shape[0] * pic.shape[1])

padding_pic = np.zeros((pic.shape[0]+2, pic.shape[1]+2, 3))

print(padding_pic.shape)
width = pic.shape[1]
height = pic.shape[0]

print(padding_pic[1:(height+1), 1:(width+1), :].shape)

padding_pic[1:height+1, 1:width+1, :] = pic
# padding_pic = padding_pic.astype(np.uint8)


edge_pic = np.zeros(pic.shape)
edge_blur_pic = np.zeros(pic.shape)
edge_blur_pic_normalized = np.zeros(pic.shape)
laplacian_pic = np.zeros(pic.shape)
sharped_pic = np.zeros(pic.shape)
sharped_sobel_pic = np.zeros(pic.shape)

for y in range(padding_pic.shape[0]-2):
    for x in range(padding_pic.shape[1]-2):
        
        subimg_r = padding_pic[y:y+3, x:x+3, 0]
        subimg_g = padding_pic[y:y+3, x:x+3, 1]
        subimg_b = padding_pic[y:y+3, x:x+3, 2]
        
        # sobel 
        gradient_r = abs(np.sum(subimg_r * sobel_gradient_y_mask)) + abs(np.sum(subimg_r * sobel_gradient_x_mask))
        gradient_g = abs(np.sum(subimg_g * sobel_gradient_y_mask)) + abs(np.sum(subimg_g * sobel_gradient_x_mask))
        gradient_b = abs(np.sum(subimg_b * sobel_gradient_y_mask)) + abs(np.sum(subimg_b * sobel_gradient_x_mask))
        
        laplacian_r = np.sum(subimg_r * laplacian_mask)
        laplacian_g = np.sum(subimg_g * laplacian_mask)
        laplacian_b = np.sum(subimg_b * laplacian_mask)
        
        # if laplacian_r > 300:
        #     print('subimg_r:', subimg_r)
        #     print('laplacian:', subimg_r * laplacian_mask)
        #     print('laplacian_r:', laplacian_r)
        
        edge_pic[y, x, 0] = gradient_r
        edge_pic[y, x, 1] = gradient_g
        edge_pic[y, x, 2] = gradient_b
              
        laplacian_pic[y, x, 0] = laplacian_r
        laplacian_pic[y, x, 1] = laplacian_g
        laplacian_pic[y, x, 2] = laplacian_b
        
        print(y, x, laplacian_r)
        
    print()


# Laplacian Sharpening...        
sharped_pic = pic + laplacian_pic
print('sharped_pic:', sharped_pic)


sharped_pic[sharped_pic > 255] = 255
sharped_pic[sharped_pic < 0] = 0
print('sharped_pic_rearange:', sharped_pic)

# sharped_pic = cv2.normalize(sharped_pic,None,0,255,cv2.NORM_MINMAX)        
# sharped_pic = sharped_pic.astype(np.uint8)
# print('sharped_pic_255:', sharped_pic)



# sharped_pic = cv2.normalize(sharped_pic,None,0,255,cv2.NORM_MINMAX)        
# sharped_pic = sharped_pic.astype(np.uint8)


# Sobel Sharpening...        
padding_pic = np.zeros((pic.shape[0]+2, pic.shape[1]+2, 3))
padding_pic[1:height+1, 1:width+1, :] = edge_pic

# 對 sobel gradient 做 average blur
for y in range(padding_pic.shape[0]-2):
    for x in range(padding_pic.shape[1]-2):
        
        subimg_r = padding_pic[y:y+3, x:x+3, 0]
        subimg_g = padding_pic[y:y+3, x:x+3, 1]
        subimg_b = padding_pic[y:y+3, x:x+3, 2]
        
        avg_r = np.sum(subimg_r * average_mask)
        avg_g = np.sum(subimg_g * average_mask)
        avg_b = np.sum(subimg_b * average_mask)
        
        edge_blur_pic[y, x, 0] = avg_r
        edge_blur_pic[y, x, 1] = avg_g
        edge_blur_pic[y, x, 2] = avg_b

        print(y, x, avg_r)
    print()

# edge_blur_pic_normalized = cv2.normalize(edge_blur_pic, edge_blur_pic_normalized)  ## 這個不會成功，與下面的 normalization 0, 1 有什麼差別？  mean 在 0 的 normalization?? 有正有負？
# edge_blur_pic_normalized2 = edge_blur_pic / np.linalg.norm(edge_blur_pic)   ## 跟上一行用 cv2 算 normalization 一樣的值
edge_blur_pic_normalized = cv2.normalize(edge_blur_pic, None, 0, 1, cv2.NORM_MINMAX)  ## 這個會成功
print('edge_blur_pic_normalized_1:\n', edge_blur_pic_normalized)


# edge_blur_pic_normalized = normalize(edge_blur_pic_normalized[:,np.newaxis], axis=0).ravel()
# print('edge_blur_pic_normalized_2:\n', edge_blur_pic_normalized)


avgMtpLapl = laplacian_pic * edge_blur_pic_normalized   # 二階微分 乘以 一階微分平均模糊
print('avgMtpLapl:\n', avgMtpLapl)


sharped_sobel_pic = pic + avgMtpLapl

edge_pic = cv2.normalize(edge_pic,None,0,255,cv2.NORM_MINMAX)        
edge_pic = edge_pic.astype(np.uint8)

edge_blur_pic = cv2.normalize(edge_blur_pic,None,0,255,cv2.NORM_MINMAX)        
edge_blur_pic = edge_blur_pic.astype(np.uint8)

# avgMtpLapl_pic = cv2.normalize(avgMtpLapl,None,0,255,cv2.NORM_MINMAX)        
# avgMtpLapl_pic = avgMtpLapl_pic.astype(np.uint8)

laplacian_pic = cv2.normalize(laplacian_pic,None,0,255,cv2.NORM_MINMAX)        
laplacian_pic = laplacian_pic.astype(np.uint8)

# cv2.imshow('gradient', edge_pic)
cv2.imwrite('output/' + img_file + "_gradient.jpg", edge_pic)

cv2.imwrite('output/' + img_file + "_gradient_blur.jpg", edge_blur_pic)

# cv2.imwrite('output/' + img_file + "_avgMtpLapl_alpha" + str(alpha) + ".jpg", avgMtpLaplc)
cv2.imwrite('output/' + img_file + "_avgMtpLapl.jpg", avgMtpLapl)

# cv2.imshow('laplacian', laplacian_pic)
cv2.imwrite('output/' + img_file + "_laplacian.jpg", laplacian_pic)

# cv2.imshow('sharped', sharped_pic)
cv2.imwrite('output/' + img_file + "_shapred.jpg", sharped_pic)

# cv2.imshow('sharped_sobel', sharped_sobel_pic)
cv2.imwrite('output/' + img_file + "_shapred_sobel.jpg", sharped_sobel_pic)

# +
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# -




