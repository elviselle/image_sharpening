# Image Sharpening - 影像銳化

### 影像的座標系不是連續，x軸座標 0, 1, 2, ..., x-1, x, x+1, ...，遞增 1。

### 單一變數，一階微分定義
<img src="https://latex.codecogs.com/gif.latex?%5Cnabla%20f%20%3D%20%5Cfrac%7B%5Cpartial%20f%7D%7B%5Cpartial%20x%7D%20%3D%20f%28x%2B1%29%20-%20f%28x%29" /> 

### 單一變數，二階微分定義
<img src="https://latex.codecogs.com/gif.latex?%5Cnabla%5E2%20f%20%3D%20%5Cfrac%7B%5Cpartial%5E2%20f%7D%7B%5Cpartial%20x%5E2%7D%20%3D%20f%28x%2B1%29%20%2B%20f%28x-1%29%20-%202%20f%28x%29" /> 

### 影像可表示為 x, y 軸兩變數的函數，f(x, y)為座標 (x, y) 的 intensity
#### 影像的二階微分定義，為在 x 方向及 y 方向上分別對 f 的兩次偏微分，然後加總。根據上式(二次微分)，得到
x 方向，<img src="https://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%5E2%20f%7D%7B%5Cpartial%20x%5E2%7D%20%3D%20f%28x%2B1%2C%20y%29%20%2B%20f%28x-1%2C%20y%29%20-%202%20f%28x%2C%20y%29" />

y 方向，<img src="https://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%5E2%20f%7D%7B%5Cpartial%20y%5E2%7D%20%3D%20f%28x%2C%20y%2B1%29%20%2B%20f%28x%2C%20y-1%29%20-%202%20f%28x%2C%20y%29" />

加總

<img src="https://latex.codecogs.com/gif.latex?%5Cnabla%5E2%20f%28x%2C%20y%29%20%3D%20f%28x%2B1%2C%20y%29%20%2B%20f%28x-1%2C%20y%29%20%2B%20f%28x%2C%20y%2B1%29%20%2B%20f%28x%2C%20y-1%29%20-%204%20f%28x%2C%20y%29" />

### Laplacian Kernel

<img src="https://latex.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7D0%20%26%20-1%20%26%200%5C%5C-1%20%26%204%20%26%20-1%20%5C%5C0%20%26%20-1%20%26%200%5Cend%7Bbmatrix%7D" />

<img src="https://latex.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7D-1%20%26%20-1%20%26%20-1%5C%5C-1%20%26%208%20%26%20-1%5C%5C-1%20%26%20-1%20%26%20-1%5C%5C%5Cend%7Bbmatrix%7D%09" /> 

### 銳化: 原圖 + Laplacian Operation(Convolution)
<img src="https://latex.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7Df%28x-1%2Cy-1%29%20%26%20f%28x%2Cy-1%29%29%20%26%20f%28x%2B1%2C%20y-1%29%5C%5Cf%28x-1%2C%20y%29%20%26%20f%28x%2C%20y%29%20%26%20f%28x%2B1%2C%20y%29%20%5C%5Cf%28x-1%2C%20y%2B1%29%20%26%20f%28x%2C%20y%2B1%29%20%26%20f%28x%2B1%2C%20y%2B1%29%5Cend%7Bbmatrix%7D" />  與 <img src="https://latex.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7D-1%20%26%20-1%20%26%20-1%5C%5C-1%20%26%208%20%26%20-1%5C%5C-1%20%26%20-1%20%26%20-1%5C%5C%5Cend%7Bbmatrix%7D%09" />  做 Convolution

#### Gradient Kernel
##### Horizontal 
<img src="https://latex.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7D-1%20%26%20-2%20%26%20-1%5C%5C0%20%26%200%20%26%200%5C%5C1%20%26%202%20%26%201%5C%5C%5Cend%7Bbmatrix%7D" /> 

##### Vritical 
<img src="https://latex.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7D-1%20%26%200%20%26%201%5C%5C-2%20%26%200%20%26%202%5C%5C-1%20%26%202%20%26%201%5C%5C%5Cend%7Bbmatrix%7D" />
