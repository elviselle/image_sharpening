# Image Sharpening - 影像銳化
### 單一變數，一階微分定義
<img src="https://latex.codecogs.com/gif.latex?%5Cnabla%20f%20%3D%20%5Cfrac%7B%5Cpartial%20f%7D%7B%5Cpartial%20x%7D%20%3D%20f%28x%2B1%29%20-%20f%28x%29" /> 
### 單一變數，二階微分定義
<img src="https://latex.codecogs.com/gif.latex?%5Cnabla%5E2%20f%20%3D%20%5Cfrac%7B%5Cpartial%5E2%20f%7D%7B%5Cpartial%20x%5E2%7D%20%3D%20f%28x%2B1%29%20%2B%20f%28x-1%29%20-%202%20f%28x%29" /> 

### 影像可表示為 x, y 軸兩變數的函數，f(x, y)為座標 (x, y) 的 intensity
，一階微分定義


### Laplacian Kernel
<img src="https://latex.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7D-1%20%26%20-1%20%26%20-1%5C%5C-1%20%26%208%20%26%20-1%5C%5C-1%20%26%20-1%20%26%20-1%5C%5C%5Cend%7Bbmatrix%7D%09" /> 

#### Gradient Kernel
##### Horizontal 
<img src="https://latex.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7D-1%20%26%20-2%20%26%20-1%5C%5C0%20%26%200%20%26%200%5C%5C1%20%26%202%20%26%201%5C%5C%5Cend%7Bbmatrix%7D" /> 

##### Vritical 
<img src="https://latex.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7D-1%20%26%200%20%26%201%5C%5C-2%20%26%200%20%26%202%5C%5C-1%20%26%202%20%26%201%5C%5C%5Cend%7Bbmatrix%7D" />
