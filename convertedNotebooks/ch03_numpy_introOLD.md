# `NumPy`: Numerical operations in Python

This tutorial uses material also found in the [SciPy 1.0 Nature Methods](https://www.nature.com/articles/s41592-019-0686-2) and [NumPy Array IEEE](10.1109/MCSE.2011.37) article and at [https://numpy.org/](https://numpy.org/).

### Learning outcomes:  - Understand Python Library `NumPy`  - Use `numpy arrays`  - Apply loops and logical operators on `numpy arrays`

Data scientists spend a lot of time – wait for it – working with ***data***! To work with **data** it is critical to organize the data in a way that facilitate the work on the potential analyses we might need to do. So organizing data means guessing what type of work we will want to do with the dataset. And, odd is it may seem, good guessing requires some practice. The data organization process will require:   * store the data a clear and systematic way * provide methods to access the data that are simple and straightforward * be flexible enough so to and allow to modify the format of the data for various needs

NumPy is the fundamental `library` for mathematical operations and computations in Python.   The NumPy library provides a series of objects that can be used to store data (represent the numbers in a dataset for Python) and a series of methods to analyze data (provide operations that can compute, say the mean or the standard deviation of some numbers in a dataset).  The NumPy `array` is the workhorse of NumPy and we will spend quite some time with it below. The numpy array is a multidimensional array object, that means that it    - (1) is an object for programming (so it has methods and proprties of an object, just like you cup holds coffee and has colors,    - (2) the Numpy array can hold data and have a bunch of properties that we can look as we look at the colors on the cup. The properties of the array help us recognize and understand what is in the array and sometimes that is really important, for example, you would not want to drink from someone else's cup, would you?  A variety of fast numerical operations on arrays are provided by NumPy. These include operations that are mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.   NumPy is the base of scientific computing and data science libraries such as [Pandas](https://pandas.pydata.org/) [scipy.org](https://scipy.org/), and [scikit-learn.org](https://scikit-learn.org/) among many others.

In other (simpler?) words, Numpy arrays are grids or tables for holding, accessing, and manipulating data. They are created and accessed in ways that are very similar to the ways Python `lists` can be accessed.  So what we are going to do is to recall how `lists` work (lists are handy!), then we will graduate to `numpy arrays` and see what they can do. 

### Python lists

We have covered Python `lists` (and other datatypes) in previous tutorials. Python `lists` (a list of things) is build by collecting, ahem, a list of things using `[square brackets]`.  For example:

```python
mylist = ['this', 3, 'list', 4+2j, 6.66]
```

We can address elements in a list by using indices and the `:` (colon) operator.

```python
mylist[0:3]
```

We can read this as "Give me all the elements in the interval between 0 **inclusive** to 3 **exclusive**."  I know this is weird. But at least for any two indexes `a` and `b`, the number of elements you get back from `mylist[a,b]` is always equal to `b` minus `a`, so I guess that's good!

We can get any consecutive hunk of elements using `:`.

```python
mylist[2:5]
```

If you omit the indexes, Python will assume you want everything.

```python
mylist[:]
```

List can obviously host also homogeneous types of data, such as `int` or `float`:

```python
mylistHomogeneous = [2, 3.14, 10.5, 11.13, 12.7, 4.31]
```

### Numpy Arrays

Numpy arrays were designed to be lists with superpowers, so almost everything we learned about  `lists` will apply to `numpy arrays` as well! The one big difference is that all elements of a `numpy array` must be of the same data type. This allows calculations on `numpy arrays` to be much faster than they would be on `lists`.

A NumPy array is a multidimensional, uniform collection of elements (that is, all elements occupy the same number of bytes in memory). An array is characterized by  - the type of elements it contains and  - its shape.    For example, a matrix might be represented as an array of shape M×N that contains numbers, such as floating-point or complex numbers. Unlike matrices, NumPy arrays can have up to 32 dimensions; they might also contain other kinds of elements (or even combinations of elements), such as Booleans or dates. [Ref. Van Der Walt et al. IEEE](10.1109/MCSE.2011.37)

Not to state the obvious, but to use `numpy arrays`, we'll need to `import` the library `numpy`. The standard is to import `numpy` as `np`:

```python
import numpy as np
```

`arrays` can be made by simply asking for one and filling it out with values, in much the same way we make a `list`.

```python
myarr = np.array([2, 4, 6, 8, 9, 10])
```

The command `print` can be used also on `NumPy arrays` and it returns the content of the array:

```python
print(myarr)
```

By simply returning the array object name (`myarr`) the output is a bit more informative and it returns the type (`array`):

```python
myarr
```

From then on, all the indexing we've learned so far applies directly! Square brackets are used for indexing and the same type of addressing can be used as we have learned for `lists`:

```python
myarr[4]
```

```python
myarr[-3:]
```

$\color{blue}{\text{Complete the following exercise.}}$    - Create a `NumPy array` containing both `int`, `float` and `complex` datatypes.    [Use the cell below to show your code]

```python

```

  - Create a `NumPy array` containing both `str` as datatypes.    [Use the cell below to show your code]

```python

```

### Operations on `numpy arrays`: the difference between `lists` and `arrays` Indeed, we can make an array directly out of a list.

```python
myArrFromList = np.array(mylistHomogeneous)
```

```python
myArrFromList
```

And then of course we can index it exactly the same way, so... *Wait, why are we making arrays now? What's the difference?*

One **huge** difference is that if we wanted to do some math with basic Python lists, the fact that they can hold multiple types of data elements does not assure that the mathematical operations will perform.

```python
mylist + 5
```

`numpy` arrays instead contain numerical elements by definition. This definition assures the ability to perform math on the arrays. So, whereas the addition above did not work when using the `list`, it does work when using the `numpy` array, even though both `list` and `array` contain the same elements!

```python
myArrFromList + 5
```

Now **that** seems like it might be useful!

$\color{blue}{\text{Complete the following exercise.}}$    - What happens when you add a number to a `NumPy array`? How do the content of the array change?    [Use the cell below to show answer the question]



  - Create a new `array` and multiply the array by a complex number:    [Use the cell below to show your code]

```python

```

    [Use the cell below to describe in your own words what happnes to the elements of the array after multiplying for a complex number]

 


### More operations on `arrays`

Two arrays can be added, or subtracted, or multiplied or whatever!

```python
myarr + myArrFromList
```

```python
myarr * myArrFromList
```

```python
myarr / myArrFromList
```

We can also **combine** our 2 arrays into a single ***two dimensional (2D) array***.

```python
twoDarr = np.array([myarr, myArrFromList])
```

```python
twoDarr
```

Simple though this may seem, *2D arrays just like this are the bedrock of data analysis!* Arrays of real data are usually larger – sometimes much much larger! – but all the principles are the same and all you as a Data Scientists need to remember is the dimensionality of the data arrays. Python will then compute what you ask for.

But, hold on one second. Remembering the dimensionality of the array is ** *very* ** imoortant. Indeed Python can perform some operations if two arrays do *not* have the same dimensions, but other operations are likely to fail.  For example, imagine two `arrays` with different dimensions:

```python
smallArray = [2, 3, 4]
largeArray = [2, 3, 4, 5, 6, 7]
```

The two arrays can be added together by using the symbol `+`:

```python
smallArray + largeArray
```

Yet, the same two arrays cannot be multiplied:

```python
smallArray * largeArray
```

This is because Python cannot identify elements to match during the multiplication.

$\color{blue}{\text{Complete the following exercise.}}$    - What happens when you add two arrays of different dimensions? Say one array with 6 complex numers and one with 4 `float` numbers?        [Use the cell below to show how to create and add the two arrays]

```python

```

    [Use the cell below to describe in your own words what happens to the arrays as result of the multiplication]



### Methods of `numpy arrays`

So the shape of the array (the dimensionality) is key, especially if we plan on doing math with the arrays, whihc is the primary goal of the arrays! 

`numpy arrays` are Python objects and as such they have `methods`. A variety of methods exist for the array and `shape` is the one that allow us to retrieve the dimensionality of an array.

```python
twoDarr.shape
```

Unlike lists, which are always just lists, arrays can come in any shape. So it's *really* convenient that they can tell us what shape they are straight away.

Indexing into 2D arrays is a straightforward extension of indexing into 1D arrays or lists. We just provide a second index after a `,` (comma). Like this.

```python
twoDarr[1,3]
```

The first index refers to the **row index**, and the second to the **column index**. In this case, we're asking for the value in the second row and the fourth column, which is indeed 7 (remember *the first row and column are index=0!*).

We can play all the same games indexing with 2D arrays as we can with 1D arrays, we just have to remember that everything before the comma `,` refers to the *rows* in that it specifies locations along the *vertical dimension*, and everything after the comma `,` refers to the *columns* in that it specifies locations along the *horizontal dimension*.

So this:

```python
twoDarr[:,0:3]
```

means "Give me all the rows (the colon `:`) in the first 3 columns (the "`0:3`)."  I told you that the colon all alone by itself would end up being useful!!! In this case for example, by using the `:` you do not need to type many indices (one per row) and you even do not need to remmeber how many rows there are, just use `:` and Python will return all the elements.

A few more examples:

```python
# the last row (regardless of the number of rows, 
# again you do not need to knowhow many rows exist)
twoDarr[-1,:] 
```

```python
twoDarr[:,-2:] # last two columns
```

```python
twoDarr[0,::2] # first row, every other column
```

To get good at this, you don't need natural born talent or anything like that. Like so much in life, the key is *practice, practice, practice*!!! So play around! You can't break your computer or anything!

Another neat trick that arrays can do is *transpose* themselves, flipping the rows for columns.  (Hold your right hand in front of your face so that you're looking at your palm with your fingers pointing towards the left. Now flip your hand so that you're looking at the back of your hand with your fingers pointing up. You just *transposed* your hand such that the first row (your pointer finger) became the first column!)

```python
colarr = twoDarr.T
```

```python
colarr
```

Why would we want to do that? By convention, *variables* in datasets should correspond to the columns, and *observations* should correspond to the rows. So we have taken data in which this was not so and turned it into an array in which the columns are the first few non-prime numbers and the prime numbers, respectively, and the rows correspond to the instances in order (1st , 2nd, 3rd, ....).  So that really speeds up a common **data wrangling** operation. 

Now that we have the data into shape, we can unleash all the powers of numpy arrays, powers which pandas DataFrames will inherit and build upon!

For example, who's bigger overall, the primes or the non-primes?

```python
colarr.sum(0)
```

The primes win!  In `colarr.sum(0)`, the 0 means "the first (vertical) dimension", i.e., sum the values *across the rows* within each column. To sum along the second dimension, we do:

```python
colarr.sum(1)
```

So any numpy array knows how to add up the numbers in it by row or by column (see what happens if you leave off the dimension, like this `colarr.sum()`. The list of things that numpy arrays can do themselves is pretty impressive.  Check it out [here](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html).  (or paste this into your browser: https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html)

$\color{blue}{\text{Complete the following exercise.}}$    - How many methods does a numpy array have? [Report your answer here]      - Create a new 2-dimensional array, and show the use of two methods not used above (`prod` and `round` could be two simple ones, but no pressure):      [Use the cell below to show how to create and add the two arrays]    *Hint:* The symbol `?` can be used at the end of a method and that can help understand how to use the method, for example, `myarray.shape?`

```python

```

### `NumPy` methods to create arrays

Often, we want to create a array that we know we're going to put values in later. For example, we might be planning on doing a computation that will result in 3 sets of 7 values, and we want be able to store them directly into an array. We can pre-make an array filled with zeros with `np.zeros(r, c)`.

```python
myzeros = np.zeros((7, 3))
```

```python
myzeros
```

Another handy method to create arrays is `ones`

```python
myones = np.ones((3,4))
```

```python
myones
```

We will encounter other `NumPy` methods in later tutorials. For the time being one last method that will turn out very handy when modelling data:

```python
myRandomNumArray = np.random.randn(10,1)
print(myRandomNumArray)
```

The `numpy` submodule `random` contains a variety of methods to create arrays containing random numbers. Generating random numbers is helpful in many applications, for example, they can be used to create normally distributed noise, or data with normally distributed noise, etc. 

$\color{blue}{\text{Complete the following exercise.}}$      - Create a new 1-dimensional array of uniformly-distributed random number:      [Use the cell below to show your code] 

```python

```

     - Create a new  2-dimensional array of normally-distributed random number:      [Use the cell below to show your code] 

```python

```

Let's now create a simple 1-D array and explore what happens when we add a number to the values and what happens when we multiply the numbers in the array:

```python
size  = 20
origArray = np.random.randn(size,1)
```

Let's look at the values in the array.

```python
print(origArray)
```

There seem to be a variety of numbers, some positive, some negative, as expected because `randn` is supposed to generate numbers centered at 0 (i.e., with mean 0) and standard deviation of 1.

Let's compute the standard deviation and mean of these numbers. Numpy provides to handy methods:

```python
mean = np.mean(origArray)
sd = np.std(origArray)
print(['The mean is:', mean])
print(['the STD is:', sd])
```

Well, okay, the mean is not quite close to 0, but perhaps close enough? The standard deviation seems pretty close to the expected value of 1.

$\color{blue}{\text{Complete the following exercise.}}$      - Create a new 1-dimensional array of 100 normally-distributed random numbers:      [Use the cell below to show your code] 

```python

```

   - What happens to the mean and standard deviation after increasing the size of the array? Are they closer of further from the expected values? Why?             [Use the cell below to show your code] 



What happens if we add 5 to the array?

```python
x  = 5 + origArray
```

```python
print(x)
```

It looks like the values shifted. But how much? It looks like they recentered at 5, the value we added. So we can perhaps assume that now the distribution of numbers is normally distributed but with a mean of 5. The standard deviation has not bee changed. It is still at 1, trust me for the moment and let try multiplying the numbers.

```python
x  = 2 * origArray
print(x)
```

It looks like the values increased. There seem to be a larger variality, more bigger numbers, both negative and positive. So perhaps the STD is not at 1 anymore. Could it be at 2?

$\color{blue}{\text{Complete the following exercise.}}$      - Compute the mean, std and median of `x`:      [Use the cell below to show your code] 

```python

```

     - What are the mean, std and median of `x`? Why, what is going on here?      [Use the cell below to show answer in your own words]



### Summary

So in this tutorial we have shown how to organize and manipulate data using Python `numpy` `arrays`.  So those are the basics of numpy arrays. They:  * store values in rows and columns * each dimension starts at index zero (like lists) * can be accessed using     - square brackets `[]` with row and column indexes separated by a comma     - integer indexes (including negative "start from the end" indexes)     - a colon `:` (or two if you want a step value other than 1) * can have maths done to every element in one go * can be added, subtracted, etc. from one another * have superpowers! they can compute stuff along their rows and columns!  The operations that are available for these two data types will be the base for many things that you might need to do as a Data Scientist. 

`Numpy arrays` Can host a variety of data types. Although this might be too much for now, below a table of all the data types an `array` can support:

| Type	| Description | | --- | --- | | bool |	Boolean (True or False) stored as a bit (0, 1) | | inti	| Platform integer (normally either int32 or int64) | | int8	| Byte (-128 to 127) | | int16	| Integer (-32768 to 32767) | | int32	| Integer (-2 ** 31 to 2 ** 31 -1) | | int64	| Integer (-2 ** 63 to 2 ** 63 -1) | | uint8	| Unsigned integer (0 to 255) | | uint16	| Unsigned integer (0 to 65535) | | uint32	| Unsigned integer (0 to 2 ** 32 – 1) | | uint64	| Unsigned integer (0 to 2 ** 64 – 1) | | float16	| Half precision float: sign bit, 5 bits exponent, and 10 bits mantissa | | float32	| Single precision float: sign bit, 8 bits exponent, and 23 bits mantissa | | float64 or float	| Double precision float: sign bit, 11 bits exponent, and 52 bits mantissa | | complex64	| Complex number, represented by two 32-bit floats (real and imaginary components) | | complex128 or complex	| Complex number, represented by two 64-bit floats (real and imaginary components) |

$\color{blue}{\text{Complete the following exercise.}}$      - Generate an 1-D array of mean = 10 and std = 1.5:      [Use the cell below to show your code]

```python

```
