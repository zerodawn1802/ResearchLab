import numpy as np
def multiplyMatrix():
	m, n = map(int, input().split())
	arr = [int(i) for i in input().strip().split()[:m * n]]
	a = np.array(arr)
	a = a.reshape(m, n)
	x, y = map(int, input().split())
	arr = [int(i) for i in input().strip().split()[:x * y]]
	b = np.array(arr)
	b = b.reshape(x, y)
	if n != x : print("None")
	else:
		res = np.matmul(a, b)
		print(res)
multiplyMatrix()