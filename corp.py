#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 13:59:38 2020

@author: elvis
"""
import cv2

img_file = 'bird_4'
# img_file = '20070401_121'
pic = cv2.imread("images/" + img_file+'.jpg')

pic_cort = pic[510: 1020, 900: 1500, :]


cv2.imwrite("images/" + img_file + "_corp.jpg", pic_cort)
