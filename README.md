# Image Sharpening - 影像銳化
> 本文與程式上傳至GitHub，連結 QR Code

![](https://github.com/elviselle/image_sharpening/blob/master/.readme_imgs/url_qrcode.png)

## 影像微分

  * ### 影像的座標系不是連續，x軸座標 0, 1, 2, ..., x-1, x, x+1, ...，遞增 1。

  * ### 單一變數，一階微分定義
    * <img src="https://latex.codecogs.com/gif.latex?%5Cnabla%20f%20%3D%20%5Cfrac%7B%5Cpartial%20f%7D%7B%5Cpartial%20x%7D%20%3D%20f%28x%2B1%29%20-%20f%28x%29" /> 

  * ### 單一變數，二階微分定義
    * <img src="https://latex.codecogs.com/gif.latex?%5Cnabla%5E2%20f%20%3D%20%5Cfrac%7B%5Cpartial%5E2%20f%7D%7B%5Cpartial%20x%5E2%7D%20%3D%20f%28x%2B1%29%20%2B%20f%28x-1%29%20-%202%20f%28x%29" /> 

  * ### 影像可表示為 x, y 軸兩變數的函數，f(x, y)為座標 (x, y) 的 intensity
    * #### 影像的二階微分定義，為在 f 分別對 x 及 y 進行兩次偏微分，然後加總。根據上式(二次微分)，得到
      * x 方向，<img src="https://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%5E2%20f%7D%7B%5Cpartial%20x%5E2%7D%20%3D%20f%28x%2B1%2C%20y%29%20%2B%20f%28x-1%2C%20y%29%20-%202%20f%28x%2C%20y%29" />

      * y 方向，<img src="https://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%5E2%20f%7D%7B%5Cpartial%20y%5E2%7D%20%3D%20f%28x%2C%20y%2B1%29%20%2B%20f%28x%2C%20y-1%29%20-%202%20f%28x%2C%20y%29" />

      * 上兩式加總，得

        <img src="https://latex.codecogs.com/gif.latex?%5Cnabla%5E2%20f%28x%2C%20y%29%20%3D%20f%28x%2B1%2C%20y%29%20%2B%20f%28x-1%2C%20y%29%20%2B%20f%28x%2C%20y%2B1%29%20%2B%20f%28x%2C%20y-1%29%20-%204%20f%28x%2C%20y%29" />

  * ### Laplacian Kernel
    * 上式影像二次微分，可以透過使用 Laplacian Kernel 進行 Convolution 達成。

    * > Laplacian Kernel
      <img src="https://latex.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7D0%20%26%20-1%20%26%200%5C%5C-1%20%26%204%20%26%20-1%20%5C%5C0%20%26%20-1%20%26%200%5Cend%7Bbmatrix%7D" />

    * > Laplacian Kernel 擴展形式
      <img src="https://latex.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7D-1%20%26%20-1%20%26%20-1%5C%5C-1%20%26%208%20%26%20-1%5C%5C-1%20%26%20-1%20%26%20-1%5C%5C%5Cend%7Bbmatrix%7D%09" /> 

---

## 銳化 <版本一>：

<img src="https://latex.codecogs.com/gif.latex?f%27%28x%2C%20y%29%20%3D%20f%28x%2Cy%29%20%2B%20%5Cnabla%5E2f%28x%2Cy%29" />

 **即 銳化 = 原圖 + (原圖與 Laplacian Kernel 擴展形式的 Convolution 運算)**

 **原圖**  <img src="https://latex.codecogs.com/gif.latex?f%28x%2Cy%29" />
<img src="images/lenna.jpg" />
 **原圖經過 Laplacian Convolution得到下圖**    <img src="https://latex.codecogs.com/gif.latex?%5Cnabla%5E2%20f%28x%2Cy%29" />
<img src="output/lenna_laplacian.jpg" />
 **銳化 <版本一>**  <img src="https://latex.codecogs.com/gif.latex?f%28x%2Cy%29%2B%5Cnabla%5E2%20f%28x%2Cy%29" />
<img src="output/lenna_sharped.jpg" />
 ### 缺點∶是銳化了，但也製造出很多雜訊!
 
---

## 銳化 <版本二>： Sobel
  * #### 銳化，但不要有雜訊。只銳化 edge 的地方，如果原本平坦的地方，有發生二階微分較高的情形，將它抹去。
  * #### 方法:
    * #### step 1) 原圖經過 Sobel Kernel 找 Edge。
    * #### step 2) Edge 經過 Average Kernel 模糊化。
    * #### step 3) 模糊化後的 Edge，標準化到 0~1 之間。
    * #### step 4) 原圖 + Lapacian * Step3。

  * #### Step 1
    * #### 原圖分別計算水平、垂直 Sobel 運算後，加總
    * #### Sobel Kernel
      * ##### Horizontal 
        <img src="https://latex.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7D-1%20%26%20-2%20%26%20-1%5C%5C0%20%26%200%20%26%200%5C%5C1%20%26%202%20%26%201%5C%5C%5Cend%7Bbmatrix%7D" /> 

      * ##### Vertical 
        <img src="https://latex.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7D-1%20%26%200%20%26%201%5C%5C-2%20%26%200%20%26%202%5C%5C-1%20%26%200%20%26%201%5C%5C%5Cend%7Bbmatrix%7D" />

    <img src="output/lenna_gradient.jpg" />

  * #### Step 2
    * #### 將 Step 1 Edge 模糊化。對 Step 1 以 Average Kernel 進行 Convolution 運算。
    * #### Average Kernel
      <img src="https://latex.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7D%5Cfrac%7B1%7D%7B9%7D%20%26%20%5Cfrac%7B1%7D%7B9%7D%20%26%20%5Cfrac%7B1%7D%7B9%7D%5C%5C%5Cfrac%7B1%7D%7B9%7D%20%26%20%5Cfrac%7B1%7D%7B9%7D%20%26%20%5Cfrac%7B1%7D%7B9%7D%5C%5C%5Cfrac%7B1%7D%7B9%7D%20%26%20%5Cfrac%7B1%7D%7B9%7D%20%26%20%5Cfrac%7B1%7D%7B9%7D%5C%5C%5Cend%7Bbmatrix%7D" />

    <img src="output/lenna_gradient_blur.jpg" />

  * #### Step 3
    * #### 將 Step 2 模糊化後的 Edge，標準化到 0~1 之間。
    * #### 使用 OpenCV 提供的 Normalization 函式
```python    
    step_3 = cv2.normalize(step_2_blur, None, 0, 1, cv2.NORM_MINMAX)    
```

  * #### Step 4
    * #### 原圖 + Lapacian * Step 3
    * #### Laplacian * Step 3 有助於將雜訊去除，只留下 edge 處要進行銳化。

    * #### 銳化效果版本二。對比原圖，細節被加強，且沒有版本一嚴重的雜訊。
    <img src="output/lenna_sharped_sobel.jpg" />

    * #### 原圖
    <img src="images/lenna.jpg" />

## 其他照片銳化效果比較
| | 20070401_121.jpg |
|-|-|
| 原圖 | <img src="images/20070401_121.jpg"/>  | 
| 銳化<br/>版本一 | <img src="output/20070401_121_sharped.jpg" /> | 
| 銳化<br/>版本二 | <img src="output/20070401_121_sharped_sobel.jpg" /> |

| | flower_1.jpg |
|-|-|
| 原圖 | <img src="images/flower_1.jpg" />  | 
| 銳化<br/>版本一 | <img src="output/flower_1_sharped.jpg"/> | 
| 銳化<br/>版本二 | <img src="output/flower_1_sharped_sobel.jpg" /> |

| | bird_4_crop.jpg |
|-|-|
| 原圖 | <img src="images/bird_4_crop.jpg" />  | 
| 銳化<br/>版本一 | <img src="output/bird_4_corp_sharped.jpg"/> | 
| 銳化<br/>版本二 | <img src="output/bird_4_corp_sharped_sobel.jpg" /> |


| | IMG_7367_2.jpg |
|-|-|
| 原圖 | <img src="images/IMG_7367_2.jpg" />  | 
| 銳化<br/>版本一 | <img src="output/IMG_7367_2_sharped.jpg"/> | 
| 銳化<br/>版本二 | <img src="output/IMG_7367_2_sharped_sobel.jpg" /> |


