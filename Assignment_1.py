#Assignment 1
import numpy as np

print("="*100)
print("---- 1. ARRAY CREATION ----")
arr_1d = np.array([10, 20, 30, 40, 50, 60])
arr_2d = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print("1D Array:", arr_1d)
print("2D Array:\n", arr_2d)
print()
print("="*100)

print("---- 2. INDEXING ----")
first_element = arr_1d[0]
last_element = arr_1d[-1]
element_2d = arr_2d[1, 2] 

print(f"First element of 1D: {first_element}")
print(f"Last element of 1D: {last_element}")
print(f"Element at row 1, column 2 in 2D: {element_2d}")
print()
print("="*100)

print("---- 3. SLICING ----")
slice_1d = arr_1d[1:4:1]
sub_grid = arr_2d[0:2, 1:3]   

print("1D Slice [1:4]:", slice_1d)
print("2D Sub-grid (Rows 0-1, Cols 1-2):\n", sub_grid)
print()
print("="*100)

print("---- 4. VECTORIZED OPERATIONS ----")
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(" a = ",a,","," b = ",b)

addition = a + b          
multiplication = a * 5    
squared = a ** 2          
sine_values = np.sin(a)   

print("Vectorized Addition (a + b):", addition)
print("Scalar Multiplication (a * 5):", multiplication)
print("Element-wise Power (a ** 2):", squared)
print("Sine values of 'a':", sine_values)
print()
print("="*100)

print("---- 5. BOOLEAN INDEXING (FILTERING) ----")
prices = np.array([15, 80, 45, 120, 30, 95])
expensive_prices = prices[prices > 50]   

print("Original Prices:", prices)
print("Prices > 50:", expensive_prices)
print("="*100)
