#in python list is implemented as dyanamic array #dynamic array is editable
#in python statistic array is not possible
#  #static array is fixed in size

#1D array
D1=[1,2,3,4,5,6,7,8,9,10]

#2D array
D2=[[1,2,3],[4,5,6],[7,8,9]]

#3D array
D3=[[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]]


print(D1)
print(D2)
print(D3)


my_array = [10, 20, 30, 40, 50]
my_array[::-1] # output: [50, 40, 30, 20, 10]
print(my_array[0])  # Output: 10 (O(1) access)

my_array.insert(2, 25)  # [10, 20, 25, 30, 40, 50] (O(n) insertion)

my_array.append(60)   # [10, 20, 25, 30, 40, 50, 60] (Amortized O(1) append)

del my_array[1]   # [10, 25, 30, 40, 50, 60] (O(n) deletion)

print(40 in my_array)  # Output: True (O(n) search)

# Using list comprehension for efficient array creation:
squares = [x**2 for x in range(10)]  # Creates an array of squares from 0 to 81.


arr = [1, 2, 3, 4, 5]
arr.remove(3)  # Removes first occurrence of 3
print(arr)  # Output: [1, 2, 4, 5]

arr.pop(2)  # Removes the element at index 2
print(arr)  # Output: [1, 2, 5]

#Linear Search: For unsorted arrays.
arr = [5, 3, 8, 6, 1]
key = 8
for i in range(len(arr)):
    if arr[i] == key:
        print(f"Element found at index {i}")
#Binary Search: For sorted arrays.
arr = [1, 2, 3, 4, 5]
low, high = 0, len(arr) - 1
key = 3

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        print(f"Element found at index {mid}")
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

