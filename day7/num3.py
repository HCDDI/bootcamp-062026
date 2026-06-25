import numpy as np

#arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
#print(arr[1, 2])
#print(arr)
#print("comparison is: \n", arr > 50)
#print("addition is: \n", arr + 10)

#arr1 = np.array([[1, 2]])
#arr2 = np.array([[1], [2], [3], [4]])
#print("shape of arr is: ", arr1.shape)
#print("shape of arr1 is: ", arr2.shape)
#print("product is: \n", arr2 * arr1)

ran = np.random.default_rng()
ints = ran.integers(6, size=4)
scores = ran.uniform(0, 100, size=4)
print(ints)
print(scores)
print("indices where scores>50:", np.where(scores > 50))
print("pass/fail:", np.where(scores > 50, "pass", "fail"))
laptops = np.array(["dell", "hp", "lenovo", "asus"])
ran.shuffle(laptops)
print(laptops)
print("index of 'dell':", np.where(laptops == "dell"))   


