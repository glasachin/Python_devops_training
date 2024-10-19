# Week 3


## Building Data Pipelines for Tensorflow-Part 1

`tf.data`: The input pipeline API

here are two distinct ways to create a dataset:
* A data source constructs a dataset from data stored in memory or in one or more files.
* A data transformation constructs a dataset from one or more `tf.data.DataSet` objects.

### Basic Mechanics
To create an input pipeline, we must start with a data source. 

`e.g.` to construct a dataset from data in memory, we can use `tf.data.Dataset.from_tensors()` or 
`tf.data.Dataset.from_tensor_slices()`. Alternatively, If our data is stored in a file then `tf.data.TFRecordDataset()`

Once we have a `Dataset Object`, we can transform it into a new Dataset by chaining method calls on the `tf.data.Dataset` object such as `Dataset.map()` and multi-element transformations such as `Dataset.batch()`. The Dataset Object is a Python iterable. 

```
dataset = tf.data.Dataset.from_tensor_slices([8,3,0,8,2,1])

for elem in dataset:
    print(elem.numpy())
```

`dataset.element_spec`


## Reading Input Data

1. using numpy arrays
2. by python generators
3. text files
4. csv files
5. by sets of files

## Batching Dataset Elements

**Simple Batching**
The simplest form of batching stacks n consecutive elements of a dataset into a single element. 

`drop_remainder` argument to ignore the last batch and get full shape propagation.


## Training workflows

**Processing Multiple Epochs**
`tf.data` API offers two main ways to process multiple epochs of the same data.

the simplest way to iterate over a dataset in multiple epochs is to use the `Dataset.repeat()` transformation.

