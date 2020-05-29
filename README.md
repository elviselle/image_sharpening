# Image Sharpening - 影像銳化

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

**銳化 = 原圖 + (原圖與Laplacian Kernel擴展形式的Convolution)**

---


#### Gradient Kernel
##### Horizontal 
<img src="https://latex.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7D-1%20%26%20-2%20%26%20-1%5C%5C0%20%26%200%20%26%200%5C%5C1%20%26%202%20%26%201%5C%5C%5Cend%7Bbmatrix%7D" /> 

##### Vritical 
<img src="https://latex.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7D-1%20%26%200%20%26%201%5C%5C-2%20%26%200%20%26%202%5C%5C-1%20%26%202%20%26%201%5C%5C%5Cend%7Bbmatrix%7D" />


## 銳化效果比較
|原圖|銳化法一|銳化法二(Sobel)|
|-|-|-|
| <img src="images/20070401_121.jpg" width="600" />  | <img src="output/20070401_121_shapred.jpg" width="600" /> | <img src="output/20070401_121_shapred_sobel.jpg" width="600" /> |
| <img src="images/lenna.jpg" width="600" />  | <img src="output/lenna_shapred.jpg" width="600" /> | <img src="output/lenna_shapred_sobel.jpg" width="600" /> |
