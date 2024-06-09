"""
- the torch runs on the GPU
"""

import torch

# scalar tensor: consists of only 1 dimension
scalar = torch.tensor(6)
print(scalar.item())

# 2 elements tensor
vector = torch.tensor([7, 7])
print(vector, vector.ndim)

# how to know the shape of the tensor
print(vector.shape, scalar.shape)

#the matrix is a 2 dimentions tensor
matrix = torch.tensor([[4, 7], [5, 6]])
print(matrix.ndim)
print(matrix.shape)

# 3 dimensions tensor
d3_tensor = torch.tensor([[[4, 7], [5, 6]], [[1, 3], [4, 8]]])
print(d3_tensor.ndim)
print(d3_tensor.shape)

# make a random tensor
# what is actually this 4,4,4 ok the first num is the size of the x axis and the second is the y
# so ex if you have 24x24 pixel image write 24,24 but what is this 3 at the end
# it is the number of channels so RBG
x_tensor = torch.rand(size=(24,24,3))
print(x_tensor)
print(x_tensor.ndim)
print(x_tensor.device)


print('-'*40)
r_tensor = torch.tensor(
    data=[1,2,3],
    dtype=torch.float64,
    device="cpu", #GPU
    requires_grad=False
)
print(r_tensor)
print(r_tensor.device)

