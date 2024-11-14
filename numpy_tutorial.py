import numpy as np
# np1 = np.array([1,2,3,4,5,6,7,8,9])
#
# # Return 2,3,4,5
#
# print(np1[1:5])
#
# # Return from something till the end of the array
# print(np1[3:])
#
# # -ve slices
# print(np1[-3:-1])
# print("\n")
# # steps
# print(np1[1:5])
# print(np1[1:5:2])
#
# # Steps on the entire array
# print(np1[::2])
# print(np1[::3])
#
# # slice a 2-d array
# np2=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(np2[1,2])
#
# # print('\n')
#
# # Slice a 2-d array
# print(np2[0:2,1:3])
#
# print("\n")
#
# # Universal function of Numpy
# import numpy as np

# np1 =np.array([0,1,2,-3,-4,-5,6,7,8,9])
#
# # print(np.sqrt(np1))
# print(np1)
# # print(np.absolute(np1))
# # print(np.exp(np1))
# # print(np.min(np1))
#
# print(np.log(np1))


# copy vs view for number
np1 = np.array([0,1,2,3,4,5])

#create a view
# np2 =np1.view()
#
# print(f"original NP1 {np1}")
# print(f"original NP2 {np2}")

# # Creating a copy
# np2= np1.copy()
# np1[0] =41
# print(f"original NP1 {np1}")
# print(f"original NP2 {np2}")

# Shape and Reshape Numpy Array
np1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(np1)
# print(np1.shape)

# np2=np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
# print(np2)
# print(np2.shape)

# # Reshape 2-D
# np3 = np1.reshape(3,4)
#
# # print(np3)
# # print(np3.shape)
#
# # Reshape in 3=D
# np4 = np1.reshape(2,3,2)
# print(np4)
# print(np4.shape)
#
# # Flatten to 1-D
# np5 = np4.reshape(-1)
# print(np5)
# print(np5.shape)

# Iterating through Numpy Arrays
import numpy as np

# 1-d
# np1 =np.array([1,2,3,4,5,6,7,8,9,10])
#
# for x in np1:
#     print(x)

# # 2-d
# np2=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# for x in np2:
#     for y in x:
#         print(y)
#
# # 3-d array
# np3 = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
# # for x in np3:
# #     for y in x:
# #         for z in y:
# #             print(z)
#
# # using np.diter()
# for x in np.nditer(np3):
#     print(x)


# Sorting numpy arrays
import numpy as np
# np1 =np.array([6,7,4,9,0,2])
# print(np.sort(np1))
#
# # Alphabetical
# np2 =np.array(['John', 'Tina','Aaron',"Zed"])
# print(np2)
# print(np.sort(np2))

# # 2 -d
# np4 =np.array([[6,7,1,9],[8,3,5,0]])
# print(np4)
# print(np.sort(np4))

# Searching through numpy array
np1 = np.array([1,2,3,4,5,6,7,8,9,3,10])

# x = np.where(np1==3)
# # print(x)
# # print(x[0])
# # print(np1[x[0]])

# Return even items
# y= np.where(np1 % 2==0)
# print(np1)
# print(y[0])

#Return odd number
# z=np.where(np1 % 2 ==1)
# print(np1)
# print(z[0])

# filtering numpy array
import numpy as np

np1 = np.array([1,2,3,4,5,6,7,8,9,10])
# x =[True,True, False,False,False,False,False,False,False,False]
# print(np1)
# print(np1[x])

# filtered = []
# for thing in np1:
#     if thing % 2 == 0:
#         filtered.append(True)
#     else:
#         filtered.append(False)
# print(np1)
# print(filtered)
# print(np1[filtered])

filtered =np1 % 2 ==1
print(np1)
print(filtered)
print(np1[filtered])
