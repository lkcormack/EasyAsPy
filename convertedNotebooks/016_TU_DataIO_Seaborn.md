## Data File I/O and Visualizing Data with Seaborn

### Learning goals

* read and write data files (pandas)
* practice exploring data (pandas + Seaborn)

In this tutorial, we will practice with reading and writing data files, and then exploring the data. These may seem like separate and unrelated steps. While they are seperate, they are by no means unrealated. In data science, we are generally dealing with data that we did not collect ourselves, so, when we get our hands on a data set, the immediate steps we take are to:

- read the data in
- examine the data as a data table/structure/data frame
- look the data visually via various plots


##### File input

Reading files from disk is more generally known as file `i/o` where `i` and `o` stand for `i`nput and `o`utput, respectively.  Why do we need to do file `i/o`?

The input case is more obvious. To analyze data, you need data to analyze. Unless you know magic, you access data from  *data files*, which are files just like a PDF documents, JPG images, or whatever, but they are specialized to some degree for containing data. Whether from a colleague, a boss, a webpage, or a government data repository, data will come in a data file that you will need to read as input in order visualize and analyze the data.

##### File output

The output case is perhaps less obvious. You read data into your Jupyter Notebook. The data are stored into Python variables. There are many different types of variables. We will learn about the fundamental ones. The variables can be used inside the Jupyter Notebook to make pretty graphs, and to do some cool analysis. But what if you want to share the numerical values, the results, of the analysis with someone else? In that case, you can write those values to a data file, save the file and send that to your colleagues.  They can then read in the values on their end without having to wade through your notebook and cutting and pasting or whatever.  

#### Import `pandas`

 Remember that, by convention, we'll import `pandas`  with the nickname `pd`. Ok, let's import `pandas`:


```python
import pandas as pd
```

    Intel MKL WARNING: Support of Intel(R) Streaming SIMD Extensions 4.2 (Intel(R) SSE4.2) enabled only processors has been deprecated. Intel oneAPI Math Kernel Library 2025.0 will require Intel(R) Advanced Vector Extensions (Intel(R) AVX) instructions.
    Intel MKL WARNING: Support of Intel(R) Streaming SIMD Extensions 4.2 (Intel(R) SSE4.2) enabled only processors has been deprecated. Intel oneAPI Math Kernel Library 2025.0 will require Intel(R) Advanced Vector Extensions (Intel(R) AVX) instructions.


 We don't *have* to do this. If wanted to, we could import pandas like this:
 ```python
 import pandas as cute_creature_that_eats_shoots_and_leaves
 ```
and the library would import just fine with the nickname `cute_creature_that_eats_shoots_and_leaves`. But, of course, whenever we wanted to use a pandas function, like `pandas.DataFrame()`, we'd have to type `cute_creature_that_eats_shoots_and_leaves.DataFrame()`.

We've already learned that `pandas` basically gives us R-like tibble (data frame) functionality in Python. But another thing Python gives us are easy ways to import and export data.

### Data preparation

For this tutorial, we are going to read a data file called `016_TU_Data1.csv`. The data was given to you and you are asked to save it inside a folder called `datasets`. The folder should be contained inside the same folder containing this Jupyter Notebook. Ideally, both `datasets` folder and Jupyter Notebook should be saved your GitHub repo.

### Let's read some data!

We are going read a file with exstension `.csv` (more on this file type in a bit) using the `pandas.read_csv()` function. But, remember, we have imported pandas as `pd`, so we read the `.csv` file, with slightly less typing, like this:


```python
myDataFromFile = pd.read_csv("./datasets/016_TU_Data1.csv")
```

This command will work "out of the box" if your copy of the data file is in your "*datasets*" directory, which should be a subdirectory of the one this notebook is in. 

Otherwise, you would have to change the command above to specify the path to the data file – where on the file tree the data file exists (either in '*absolute*' terms from root, or in '*relative*' terms from you current directory).

Once you start reading an writing data files, it'll quickly become clear how important having an organized directory structure is!

$\color{blue}{\text{Answer the following questions:}}$

Just to be super clear that we all see what is going on, in the line of code above, what is the:

 - name of the library used to load the file?  [Enter answer here]
 - name of the `pandas` function we use to read the data file?  [Enter answer here]
 - data file name?  [Enter answer here]
 - name of the variable used to store the file?  [Enter answer here]
 - name of the folder containing the data file?  [Enter answer here]

### Let's look at what we just read.

Okay, now let's look at the file. We can take a quick peek by using the `display()` function:


```python
display(myDataFromFile)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>VarA</th>
      <th>VarB</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.979109</td>
      <td>-0.128890</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.196564</td>
      <td>0.403177</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.260841</td>
      <td>0.682448</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2.432641</td>
      <td>-0.295968</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.689790</td>
      <td>-0.088941</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>95</th>
      <td>2.416932</td>
      <td>-1.065406</td>
    </tr>
    <tr>
      <th>96</th>
      <td>4.166266</td>
      <td>-1.053911</td>
    </tr>
    <tr>
      <th>97</th>
      <td>-0.203719</td>
      <td>0.610032</td>
    </tr>
    <tr>
      <th>98</th>
      <td>1.232813</td>
      <td>-0.744738</td>
    </tr>
    <tr>
      <th>99</th>
      <td>0.833993</td>
      <td>-0.372451</td>
    </tr>
  </tbody>
</table>
<p>100 rows × 2 columns</p>
</div>


Here, we can see that this file (like almost all data files) consists of rows and columns. The rows represent *observations* and the columns represent *variables*. This type of data file contains "tidy" data (if you have used R, you may have encountered the tidyverse). Sometimes, we will encounter data files that violate this "rows = observations, columns = variables" rule – untidy data – we will deal with this issue later in the class.

$\color{blue}{\text{Answer the following question:}}$

 - What are the dimensions (the size) of the data?  [Type the Answer here]

A very common genertic data file type is the comma separated values file, or .csv file. This is the type of data file we just loaded (016_TU_Data1***.csv***). As the name implies, a file in this format consists values separated by commas to form rows, and "carriage returns" (CR) or "line feeds" (LF) marking the end of each row.

---
**Useless Trivia Alert!**:

These terms come from typewritters and old-old-old-school printers, respectively. Typewritters had a "carriage" that held the paper and moved to the left while you typed. When you got to the right edge of the paper, you hit the "*carriage return*" key and the whole carriage flew back (*returned*) to right with a loud clunk and advanced the paper down a line. To this day, the big fat important key on the right side of most keyboards still says "return".

Old-school printers used long continuous "fan fold" sheets of paper (they could be literally hundreds of feet long) and had to be told to advance the paper one line with a "*line feed*" command. Once you were done printing, you ripped/cut your paper off the printer sort of like you do with aluminum foil or plastic wrap!

---

### Reading data from the clipboard

When you copy something to the clipboard of your computer, it goes into a file – it's a special file that the computer manages for you, but it's a file nonetheless. When you paste what you copy, data are read from that file and put where you asked it to go.

Very conveniently, `pandas` has a function to read data into a data frame directly from the clipboard! 

Go to Wikipedia and copy the table of the [population of Burkina Faso by year](https://en.wikipedia.org/wiki/Demographics_of_Burkina_Faso). 

After that, you can read the data from Wikipedia Table into a `pandas` data frame like this:


```python
cb = pd.read_clipboard()
```


```python
cb
```

How cool is that?!?!

### data frame methods

In addition to `display()`, we use can use data frame "methods". 

Remember, "methods" are things that an object, like a `pandas` data frame, can do. They are actions that an object can perform for us without any additional coding on our part!

Also recall that methods  are invoked using the following syntax `ObjectName.MethodName()`.

One thing a data frame knows how to do is show you its first few rows with the `head()` method. This method returns the top (leading, or head of a data table):


```python
myDataFromFile.head()
```

Another method is `tail()`. This second method shows the last rows of the table:


```python
myDataFromFile.tail()
```

But how do you know what methods a given object has? In addition to the tab key trick, Python's `dir()` function will give you a directory of any objects methods:


```python
dir(myDataFromFile)
```

Wow!!! Data frames know how to do a LOT! It's a bit overwhelming actually. 

We can ignore all the things that look like \_\_this\_\_ at the top. Scrolling through the others, we see our old friend `describe()`.


```python
myDataFromFile.describe()
```

$\color{blue}{\text{Answer the following question:}}$

 - Describe in your own words what the method describe returns of the data. Describe the measures the method returns.
 
 [Type the Answer here]

There is also  a `hist` method. Could it even be possible that data frames know how to draw histograms of themselves?


```python
myDataFromFile.hist()
```

Okay, that's *awesome*.

As you can see, our journey of learning to play with data is going to be part learning to code and part figuring how to use what's already out there!

$\color{blue}{\text{Answer the following questions:}}$

 - What are the titles of the two histograms in the figures created by the method `.hist`?  [Type the answer here]
 - How do the titles of the histograms relate to the data? [Type the answer here]
 - What are the values represented by the y-axis of the histograms? [Type the answer here]

### Writing data to a file

Now maybe we can write a summary of the original data to a file so we could potentially share it with other. What we'll do is use the `describe()` method again, but this time we'll assign it to new data frame.


```python
mySummary = myDataFromFile.describe()
```

Let's just quickly confirm that `mySummary` contains what we hope it does. The python command `print` will help us take a look at the summary:


```python
print(mySummary)
```

See what we did above? Instead of returning the results of the method `.describe()` directly in the notebook output, we saved the output into a variable. We then used `print` to display the content of the variable.

Next let's write the variable to a file! Given that we are dealing with a table, we will save the variable in a `.csv` file. The variable has a method `.to_csv`, the method can be found by lurking the output of `dir(<varName>)`.


```python
mySummary.to_csv("mySummary.csv")
```

Okay, but how do we know that worked? Easy! We'll read that file back in using `pandas.read_csv()` and see what it looks like!


```python
mySummary2 = pd.read_csv("mySummary.csv")
```

And then we can look at it using `display()`.


```python
display(mySummary2)
```

**We can now both read and write data files. That adds a powerful pair of tools to our data science toolbox**

## Seaborn overview

`Seaborn` is a package meant to provide a facilitatated access to plotting data. It's like an add-on to `pandas` to accelarate data exploration via visualiation.

`Seaborn` was written to:

* make plots from `pandas` data frames
* create good looking plots "out of the box"

The `seaborn` package is a "high level" plotting package that makes good looking plots while taking care of many details for you under the hood, so making basic plots is easy. If we want fine control over our plots, we need to go another direction, but we'll learn about that later.

The various `seaborn` functions are conceptually structured like this:
![seaborn_overview](./assets/jpnb20/seabornOverview.png)

The three columns correspond to plot types: plots of relationships, plots of data distributions, and plots of categorical data. 

For each plot type, there is a high level function, `relplot()`, `displot()`, and `catplot()`. These pretty much make a figure for you without you having to worry about anything. Technically, they are "figure level" functions.

In addition to the 3 high level functions, there are specific functions (technically "axes level" functions) for making each specific kind of plot directly. Each of these returns an `axes` object, which you can then modify further if you need to.

Don't worry about exactly what "figure level" and "axes level" mean right now – we'll get to that when we get to that – for now, just think of the figure level functions as high-level functions that make a bunch of decisions for you, and axes level functions as the ones you call when you know exactly what kind of plot you want make, and wish to customize it further after you've made it.

First, let's import what we'll need:


```python
import pandas as pd
import seaborn as sns
```

Here we have another naming convention: although you can call `seaborn` whatever you wish, `sns` is the recommended nickname.

---

Geek trivia: `seaborn` is named for Sam Seaborn, a character on a very highly regarded show called The West Wing. He was both very smart and good looking, which is what `seaborn` aspires to be. His full name was Samuel Norman Seaborn, hence `sns`.

---


```python
our_data = pd.read_csv("./datasets/016_TU_Data2.csv")
```

Let's take a quick peak at the data.


```python
our_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>RTs</th>
      <th>sex</th>
      <th>strain</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>10.485451</td>
      <td>M</td>
      <td>Wild Type</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>11.747948</td>
      <td>M</td>
      <td>Wild Type</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>13.412580</td>
      <td>M</td>
      <td>Wild Type</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>12.910095</td>
      <td>M</td>
      <td>Wild Type</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>10.367770</td>
      <td>M</td>
      <td>Wild Type</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>11.698422</td>
      <td>M</td>
      <td>Wild Type</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>11.583153</td>
      <td>M</td>
      <td>Wild Type</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>11.447349</td>
      <td>M</td>
      <td>Wild Type</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>10.852276</td>
      <td>M</td>
      <td>Wild Type</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9</td>
      <td>11.285897</td>
      <td>M</td>
      <td>Wild Type</td>
    </tr>
    <tr>
      <th>10</th>
      <td>10</td>
      <td>8.250013</td>
      <td>F</td>
      <td>Wild Type</td>
    </tr>
    <tr>
      <th>11</th>
      <td>11</td>
      <td>8.453839</td>
      <td>F</td>
      <td>Wild Type</td>
    </tr>
    <tr>
      <th>12</th>
      <td>12</td>
      <td>9.706605</td>
      <td>F</td>
      <td>Wild Type</td>
    </tr>
    <tr>
      <th>13</th>
      <td>13</td>
      <td>9.522116</td>
      <td>F</td>
      <td>Wild Type</td>
    </tr>
    <tr>
      <th>14</th>
      <td>14</td>
      <td>8.583212</td>
      <td>F</td>
      <td>Wild Type</td>
    </tr>
    <tr>
      <th>15</th>
      <td>15</td>
      <td>9.835002</td>
      <td>F</td>
      <td>Wild Type</td>
    </tr>
    <tr>
      <th>16</th>
      <td>16</td>
      <td>10.532096</td>
      <td>F</td>
      <td>Wild Type</td>
    </tr>
    <tr>
      <th>17</th>
      <td>17</td>
      <td>9.394166</td>
      <td>F</td>
      <td>Wild Type</td>
    </tr>
    <tr>
      <th>18</th>
      <td>18</td>
      <td>8.739473</td>
      <td>F</td>
      <td>Wild Type</td>
    </tr>
    <tr>
      <th>19</th>
      <td>19</td>
      <td>10.892394</td>
      <td>F</td>
      <td>Wild Type</td>
    </tr>
    <tr>
      <th>20</th>
      <td>20</td>
      <td>20.127063</td>
      <td>M</td>
      <td>Mutant</td>
    </tr>
    <tr>
      <th>21</th>
      <td>21</td>
      <td>20.068147</td>
      <td>M</td>
      <td>Mutant</td>
    </tr>
    <tr>
      <th>22</th>
      <td>22</td>
      <td>21.215148</td>
      <td>M</td>
      <td>Mutant</td>
    </tr>
    <tr>
      <th>23</th>
      <td>23</td>
      <td>20.706416</td>
      <td>M</td>
      <td>Mutant</td>
    </tr>
    <tr>
      <th>24</th>
      <td>24</td>
      <td>18.074795</td>
      <td>M</td>
      <td>Mutant</td>
    </tr>
    <tr>
      <th>25</th>
      <td>25</td>
      <td>20.367624</td>
      <td>M</td>
      <td>Mutant</td>
    </tr>
    <tr>
      <th>26</th>
      <td>26</td>
      <td>20.152521</td>
      <td>M</td>
      <td>Mutant</td>
    </tr>
    <tr>
      <th>27</th>
      <td>27</td>
      <td>19.392476</td>
      <td>M</td>
      <td>Mutant</td>
    </tr>
    <tr>
      <th>28</th>
      <td>28</td>
      <td>18.524341</td>
      <td>M</td>
      <td>Mutant</td>
    </tr>
    <tr>
      <th>29</th>
      <td>29</td>
      <td>20.325026</td>
      <td>M</td>
      <td>Mutant</td>
    </tr>
    <tr>
      <th>30</th>
      <td>30</td>
      <td>25.946384</td>
      <td>F</td>
      <td>Mutant</td>
    </tr>
    <tr>
      <th>31</th>
      <td>31</td>
      <td>23.464870</td>
      <td>F</td>
      <td>Mutant</td>
    </tr>
    <tr>
      <th>32</th>
      <td>32</td>
      <td>22.989480</td>
      <td>F</td>
      <td>Mutant</td>
    </tr>
    <tr>
      <th>33</th>
      <td>33</td>
      <td>25.324376</td>
      <td>F</td>
      <td>Mutant</td>
    </tr>
    <tr>
      <th>34</th>
      <td>34</td>
      <td>22.607487</td>
      <td>F</td>
      <td>Mutant</td>
    </tr>
    <tr>
      <th>35</th>
      <td>35</td>
      <td>23.052187</td>
      <td>F</td>
      <td>Mutant</td>
    </tr>
    <tr>
      <th>36</th>
      <td>36</td>
      <td>25.369037</td>
      <td>F</td>
      <td>Mutant</td>
    </tr>
    <tr>
      <th>37</th>
      <td>37</td>
      <td>23.372709</td>
      <td>F</td>
      <td>Mutant</td>
    </tr>
    <tr>
      <th>38</th>
      <td>38</td>
      <td>25.215646</td>
      <td>F</td>
      <td>Mutant</td>
    </tr>
    <tr>
      <th>39</th>
      <td>39</td>
      <td>24.990505</td>
      <td>F</td>
      <td>Mutant</td>
    </tr>
  </tbody>
</table>
</div>



These data are response times (completion times) for rats in a "water maze" (basically a tank of water containing a hidden platform – a rat must swim around until it finds the platform). Responses have been recorded both male and female rats of two genetic strains, wild and mutant.

Notice that our data also have an unnamed that is also unecessary because it is redundant with the index. This kind of thing happens all the time in data science! Outside of the classroom, it's more often than not that will have to "clean" and "wrangle" the data set before we can start actually diving into it!

Happily for us, `pandas` data frames have a `drop()` method specifically to get rid of unwanted columns. Let's do that:


```python
our_data = our_data.drop(columns=['Unnamed: 0'])
```

And check:


```python
our_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>RTs</th>
      <th>sex</th>
      <th>strain</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10.485451</td>
      <td>M</td>
      <td>Wild Type</td>
    </tr>
    <tr>
      <th>1</th>
      <td>11.747948</td>
      <td>M</td>
      <td>Wild Type</td>
    </tr>
    <tr>
      <th>2</th>
      <td>13.412580</td>
      <td>M</td>
      <td>Wild Type</td>
    </tr>
    <tr>
      <th>3</th>
      <td>12.910095</td>
      <td>M</td>
      <td>Wild Type</td>
    </tr>
    <tr>
      <th>4</th>
      <td>10.367770</td>
      <td>M</td>
      <td>Wild Type</td>
    </tr>
  </tbody>
</table>
</div>



## Figure level plots

 We'll start with some figure level plots.

### Distribution plots

#### Histogram of the RTs
We'll start interrogating the data with a histogram of the lone numerical variable, the RTs


```python
sns.displot(x = "RTs", data = our_data);
```

Okay, here we can see that there are two clumps of data. Let's see if they correspond to one or more of the categorical variables.

#### Histogram of RTs by one of the categorical variables
We'll use color ("hue" in seaborn-speak) to code the categorical variable "sex".


```python
sns.displot(x = "RTs", data = our_data, hue = "sex");
```

Okay, there might be something going on with females being both faster (left) and slower (right) than males, but there's still something going on here that "sex" isn't capturing. Let's see if "strain" does.

#### Histogram of RTs by the other categorical variable
Now we'll use color ("hue" in seaborn-speak) to code the categorical variable "strain".


```python
sns.displot(x = "RTs", data = our_data, hue = "strain");
```

**Aha!** **Gotcha** – it looks like strain is doing a pretty good job of explaining the two clumps in the histogram. But the histogram of RT x Sex still did look a litte weird. Let's see if we can crack out both variables.

#### Creating a multi-axes figure with a figure level seaborn function

This is where the figure level `seaborn` functions are really handy. We can simply assign a categorical variable to be represented by the columns or rows to make a multi-panel figure (hence the name "figure level").

Let's assign "sex" to columns.


```python
sns.displot(x = "RTs", data = our_data, hue = "strain", col="sex");
```

Okay, that's great. Now we have males on the left and females on the right. Also, `displot()` has done something really nice, which is to make the x-axis limits the same in the two plots. So the bigger gap in the female data isn't just a visual artifact of the axis scaling.

Still, since the data share a common x-axis, it would be nice to have the plots aligned vertically rather than horizontally. So let's assign sex to the rows rather than the columns.


```python
sns.displot(x = "RTs", data = our_data, hue = "strain", row="sex");
```

Okay, that last plot we made above was much better in terms of making a visual comparison between the sexes. Still, these histrograms are a bit ugly. We could improve that by playing around with the bins. Or we could just ask `displot()` to give us "kernel density estimates" (KDEs) instead. KDEs are a (quasi) continuous version of histogram. The algorithms that make them make certain assumptions about the data are distributed locally, and then try to estimate the true probability density function of the data.


```python
sns.displot(x = "RTs", data = our_data, hue = "strain", row="sex", kind="kde");
```

Much better! Visually, however, filled KDE's are a bit nicer. Since these are probability *densities*, it's the area that's important anyway, and having them filled emphasizes the area rather than the height.

We can easily do this by setting a `fill` argument to `True`. Strictly speaking, however, `fill` is not a valid argument to `displot()`. However, what displot will do is pass any named argument (called a "keywork arguement" or "kwarg" in Python) to the underlying axes level function.

The only catch with these `**kwargs` is that they won't appear in the documentation for the figure level plots, only in the documentation for the axes level plots. The documentation for the figure level [plot](https://seaborn.pydata.org/generated/seaborn.displot.html#seaborn.displot), like `displot()` does helpfully tell us this at least:

---

![displot() kwargs](./assets/jpnb20/displotKwargs.png)

---

So now let's plot with `fill=True` and see if that works.


```python
sns.displot(x = "RTs", data = our_data, hue = "strain", row="sex", kind="kde", fill=True);
```

Ah, much better!

---

$\color{blue}{\text{Complete the following exercise.}}$

 - Use the cell below to show an example plot that uses the data above in combination with the `seaborn` parameter `ecdf`.


```python

```

 - If you belive the parameter cannot be used in combination with the data at hand, use the cell below to explain the reason why the parameter cannot be properly used in this case.



---

### Categorical plots

The categorical plots are nice because they allow us to separate both of our categorical variables within a single plot.

Let's try playing with `catplot()`


```python
sns.catplot(y = "RTs", x="strain", data = our_data, hue = "sex");
```

So a `stripplot` is the default axes-level plot (and notice that the default axes-level plots are the first ones listed under their corresponding figure-level counterparts in the `seaborn` stucture chart). But we can have it make a boxplot, violin plot, etc., by using the `kind` parameter.


```python
sns.catplot(y = "RTs", x="strain", data = our_data, hue = "sex", kind="violin");
```

### Axis level plots

We can call any of the axis-level functions directly, without going through the corresponding figure-level function. This gives us more control over single-panel plots should we need it.


```python
ax = sns.boxplot(y = "RTs", x="strain", data = our_data, hue = "sex");
```

Notice that we've assigned the output of `sns.boxplot()` to `ax`. So now we have an `axes` object (named `ax`), and thus have access to all the things an `axes` knows how to do. So if we type "ax." and a tab (or `dir(x)`), we'll see something like this:
    
---
    
![seaborn_overview](./assets/jpnb20/axesMethods.png)
    
---

So let's do that:


```python
dir(ax)
```

and now we can scroll around to find useful things. 

Let's try inverting the y axis so that faster times plot visually higher!


```python
ax = sns.boxplot(y = "RTs", x="strain", data = our_data, hue = "sex");
ax.invert_yaxis();
```

Also among these methods is an `ax.set_title()` which we can use to... wait for it... add a title!


```python
ax = sns.boxplot(y = "RTs", x="strain", data = our_data, hue = "sex");
ax.invert_yaxis();
ax.set_title("Response time by sex and strain - higher is faster");
```

### Summary
So `seaborn` is a nice way to make plots of data from `pandas` data frames. Its default values make good looking plots. It has two main kinds of plotting functions:

* figure level functions that are handy for making multi axes panel figures
* axes level functions that return an axes object handle to you, allowing for fine control over the plot's appearance



---

### Overall summary

We've learned a couple powerful things today, namely

- file I/O for csv files (and input from the clipboard) using `pandas`
- examining a data set visually using `seaborn`

We'll be learning about and using other libraries as we go, but the combination of `pandas` and `seaborn` will actually get you pretty far in analyzing a wide array of data sets.
