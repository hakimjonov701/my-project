import numpy as np

# 1. Massiv yaratish
array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])  # 2D massivni o'z holida qoldirdim

# 2. Matematik operatsiyalar (1D massiv)
sum_array = np.sum(array_1d)
mean_array = np.mean(array_1d)
product_array = np.prod(array_1d)

# Natijalarni chop etish
print("1D Massiv: ", array_1d)
print("2D Massiv:\n", array_2d)
print("Massiv yig'indisi (1D): ", sum_array)
print("O'rtacha (1D): ", mean_array)
print("Ko'paytma (1D): ", product_array)
