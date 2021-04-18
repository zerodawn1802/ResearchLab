import numpy as np
m, n = map(int, input().split())
arr = [int(i) for i in input().strip().split()[:m * n]]
a = np.array(arr)
a = a.reshape(m, n)
print("Giá trị lớn nhất trên mỗi hàng:", np.amax(a, axis = 1))
print("Giá trị nhỏ nhất trên mỗi cột:", np.amin(a, axis = 0))
k = min(m, n)
print("Tổng đường chéo chính:", sum(a[i][i] for i in range(k)))