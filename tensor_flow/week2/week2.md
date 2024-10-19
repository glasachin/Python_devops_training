# Week 2

1. Underfit
2. Just Right
3. Overfit

## Deep Learning

large model with more training data.

## Introduction to tensors

1. Tensor is a container for data, where we store almost always numerical data.
2. Tensors are a generalization of matrices to an arbitrary number of dimensions (ie. axis or rank).

A Tensor is defined by three attributes:
1. Number of axes or rank (ndim)
2. Shape (shape)
3. Data Type (dtype)

### Scalars (0D Tensors)
A tensor that contains only one number is called scalar or scalar tensor or 0D tensor
```
x = np.array(10)
x.shape
x.ndim
x.dtype
```

### Vectors (1-D Tensors)

```
x = np.array([3,4,5])
x.shape
```

### Matrices (2-D Tensors)
An array of vectors is a matrix or 2-D Tensor.

```
x = np.array([[1,2,3],
               [3,4,5],
               [3,4,5]])
x.shape
x.ndim
```
black and white image are 2-D tensor

### 3-D Tensors
i.e. 3D array

color images are a good example of 3-D array.

### Tensor Slicing (Data Selection)

similar to accessng the data from and array or list.

NOTE: Complete training data in an array can be termed as a tensor as well, i.e. a variable containing 90 images.

### Data Batches
We usually break the data into small batches and process those batches:
* Thefirst axis in all data sensor is sample axis or sample dimension.
* The first axis of batch tensor is called the batch axis or batch dimension.

