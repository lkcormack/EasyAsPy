Ch. 3 – Numpy puzzles



### **Comparing Conditions**

Let’s compute the differences between conditions:

```python
# Mean difference between Lie and Truth conditions for GSR
gsr_diff_lie_truth = np.mean(data[:, 2]) - np.mean(data[:, 0])
print("GSR Mean Difference (Lie - Truth):", gsr_diff_lie_truth)

# Mean difference between Lie and Control conditions for HR
hr_diff_lie_control = np.mean(data[:, 5]) - np.mean(data[:, 4])
print("HR Mean Difference (Lie - Control):", hr_diff_lie_control)
```

###