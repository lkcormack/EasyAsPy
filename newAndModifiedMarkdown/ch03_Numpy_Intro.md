# Chapter 3 - NumPy

---

## **Introduction**
Here we meet **[NumPy](https://numpy.org/)** – **Num**erical **Py**thon – a Python library for numerical computation. When we say “numerical”, we mean *numerical*; No automatic conversion to `ord` values, no indexes, no strings (ha) – just numbers. In fact, Pandas relies on numpy as its numerical engine – one way of thinking of Pandas is as an extension of numpy that allows non-numerical data to be stored along with numerical data, giving us an R-like data frame to work with. Numpy, on the other hand, was to work with large *numerical* data sets.  

# A brief history of NumPy

Numpy was born in 2005 – well, not really born – it was created by Travis Oliphant, who took the best parts of 2 existing libraries, combined them, and addressed some shortcomings of each. One of those existing libraries (called Numarray) was written at the [Space Telescope Science Institute](https://www.stsci.edu/home) to handle the massive datasets that astronomical studies produce. Numpy quickly became the Python standard for numerical computation. It is now such a core library that not only is Panda’s built atop of it, but so are scikit-learn and Sci-Py, 2 libraries you will soon meet if you continue your data science journey!

---

# Our mission

In this chapter, we’ll be using a pre-generated dataset from a simulated lie detector test. You’ll learn:

1. The simple structure of a numpy array.
2. How to manipulate and analyze data with numpy.
3. How to slice subsets of data from arrays (don’t panic – it’s like with lists)
4. Compute summary statistics on the data
5. Get a peek-ahead of visualizing results with [matplotlib](https://matplotlib.org/), a ubiquitous Python package for scientific data visualization.

---

## **The Dataset**

The dataset contains (simulated) physiological responses from 100 participants in a lie detector test. Each participant completed three *conditions*:
- **Truth**: the participants answered truthfully
- **Control**: the participants said something random
- **Lie**: being LAMbs, we can probably deduce what this condition was

The responses (or measurement types) were:
1. **GSR (Galvanic Skin Response)**: Measured in microSiemens (µS).
2. **HR (Heart Rate)**: Measured in beats per minute (BPM).
3. **RR (Respiratory Rate)**: Measured in breaths per minute.
4. **PD (Pupil Diameter)**: Measured in millimeters (mm).

The data are in a csv file with 100 rows (one for each participant) and 12 columns. This table describes the columns:

| Column Index | Data Type  | Description                          |
|--------------|------------|--------------------------------------|
| 0–2          | GSR        | Galvanic Skin Responses for Truth, Control, Lie |
| 3–5          | HR         | Heart Rate values for Truth, Control, Lie |
| 6–8          | RR         | Respiration Rate values for Truth, Control, Lie |
| 9–11         | PD         | Pupil Diameter values for Truth, Control, Lie |

---

##  Loading the Data

Huge surprise! – we’ll start by loading the dataset… The first thing to notice – right there on line 1! – is that we `import numpy` with the nickname `np`. You don’t *have* to do this (it’s Python after all), but the whole entire Python community uses `np` so, even if you have a wicked non-conformist streak, everybody including you will be happier if you just use `np`. Copy or type this code in and run it – make sure you have the data file in your “datasets” folder where it belongs! 

```python
import numpy as np

# Load the dataset
# need to change np.load for reading a CSV?
data = np.load("datasets/lie_detector_data.npy")

```

Now we can view the `numpy` `data.shape` property to make sure our data array has the right number of rows and columns: 

```python
# Confirm the shape of the array
print("Data shape:", data.shape)

```

And we can look at the first 5 rows of the data like this (which should look reassuringly familiar!).

```python
# View the first 5 rows
print("First 5 rows of the data:")
print(data[:5]) 

```

These 2 code blocks just gave you a little peek at what’s coming! The first shows 1 of the properties (nouns or “attributes”) that numpy arrays have, and the second gave you a little preview of *slicing*, which we’ll tackle next.

---

##  Exploring the Data

###  Slicing (and dicing!)

Slicing works similarly to how it does with Python lists, except for 2 little things:

* When you want to slice every other number, every 3rd number, etc., slicing goes `[start:step:stop]` instead of `[start:stop:step]` – not gonna lie, the `numpy` way makes a lot of sense.
* With `numpy` arrays, we need to “worry” about that second dimension! All this means is that *slicing a NumPy array is like cutting a cake*, whereas *slicing a regular Python list is like snipping a string*.

Fear not! 2D indexing is but a logical extension of 1D indexing, with a second index range to specify the columns of the 2D array. For example: `data[0:5, 0:3]` would the first 5 rows and the first 3 columns.

Let’s view some subsets of the array using slicing. We’ll assign our slices (pieces of cake) descriptive names:

```python
# Access GSR values for all participants
gsr_data = data[:, 0:3]
print("GSR data (first 5 rows):\n", gsr_data[:5])

# Access HR values for all participants
hr_data = data[:, 3:6]
print("HR data (first 5 rows):\n", hr_data[:5])

```

No biggie, right?

Other things we might want to do with these data are look at them by participant. We can easily do this just by specifying a row index – if you omit the column index, `numpy` will just assume you mean “all columns”!

```python
# Access data for the first participant
participant_1 = data[0] # same as ... = data[0, :]
print("Participant 1's data:", participant_1)

```

Of course, we could also look by condition; we just have to grab the appropriate columns, which are not adjacent.

```python
# Access Lie condition data for all responses
lie_data = data[:, [2, 5, 8, 11]] 
print("Lie condition data (first 5 rows):\n", lie_data[:5])

```

Is there a better way to get every 3rd column? If you think so, keep that answer in mind – it might pop up in a puzzle!

---

### **Examples of basic statistics**

NumPy makes it easy to compute statistics across rows or columns.
```python
# Mean and standard deviation for each response type (GSR, HR, RR, PD)
gsr_mean = np.mean(gsr_data, axis=0) # can omit axis arg; 0 is default
gsr_std = np.std(gsr_data, axis=0)
print("GSR Mean (Truth, Control, Lie):", gsr_mean)
print("GSR Std Dev (Truth, Control, Lie):", gsr_std)

```

To compute the mean and std. dev. of GSR *across conditions* for each participant, we’ll flip the axis along which we compute our statistics:

```python
P_GSR_means = np.mean(hr_data, axis=1) # note change of axis to 1
P_GSR_std = np.std(hr_data, axis=1)
print("HR Mean (Truth, Control, Lie):", hr_mean)
```

As you might imagine, NumPy has other functions to operate on rows or columns, and you can probably guess some of their names.

### Further Analyses

NumPy also has many (many, many) functions for analyzing data. It is “numerical Python” after all! One example that will be immediately familiar is the correlation between 2 variables (columns):
```python
# Correlation between GSR and HR in the Lie condition
gsr_lie = data[:, 2]
hr_lie = data[:, 5]
lie_corr = np.corrcoef(gsr_lie, hr_lie)
print("Correlation (GSR vs HR in Lie condition):", lie_corr[0, 1])
```

Raise your hand if you know why `lie_corr`is a matrix, and why we are only printing the upper-right corner of that matrix! 

Okay, you can put your hand down now.

---

## **Visualizing data**

### **Box Plot**

```python
import matplotlib.pyplot as plt

# Box plot for GSR responses
plt.boxplot([data[:, 0], data[:, 1], data[:, 2]],
            labels=['Truth', 'Control', 'Lie'])
plt.title("GSR Responses Across Conditions")
plt.ylabel("GSR (µS)")
plt.show()
```



### **Simple Plot**

```python
# Mean responses for each condition
gsr_means = np.mean(gsr_data, axis=0)

plt.plot(['Truth', 'Control', 'Lie'], gsr_means, marker='o')
plt.title("Mean GSR Across Conditions")
plt.ylabel("Mean GSR (µS)")
plt.show()
```

---

## **7. Saving Processed Results**

Save processed data and summaries for further use:
```python
# Save summary statistics
summary_data = {
    "Condition": ["Truth", "Control", "Lie"],
    "GSR_Mean": np.mean(gsr_data, axis=0),
    "HR_Mean": np.mean(hr_data, axis=0)
}

np.save("summary_statistics.npy", summary_data)
print("Summary statistics saved.")
```

---

## **Conclusion**

In this chapter we dipped out toes into NumPy arrays, including:
1. Slicing subsets of data.
2. Performing simple analyses
3. we also got a glimpse of visualizing results with Matplotlib, which is the topic of the next chapter.
4. 
