import numpy as np

# Create a numpy array
array = np.random.rand(10, 5)

# Print the first 5 rows of the array
print(f"orig array: \n {array[:4, :3]}")
aView = array[:4, :3].copy()
print(f"view: \n {aView}")

# Modify the view
aView[0, :] = 1000
print(f"view after mod: \n {aView}")
print(f"orig array after mod: \n {array[:4, :3]}")

print(f"ax 0 mean: {np.mean(aView, axis=0)}")
print(f"ax 1 mean: {np.mean(aView, axis=1)}")

# np.save("array.npy", array)

