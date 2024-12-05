# make a simulated dataset for GSR

import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Simulate physiological responses
n_participants = 100
conditions = ['Truth', 'Control', 'Lie']

def simulate_responses(n, mu, sigma):
    """
    Simulate physiological responses using a normal distribution.
    n: Number of participants
    mu: Mean of the distribution
    sigma: Standard deviation of the distribution
    """
    # Create a 2D array for easy slicing
    data = np.column_stack(conditions, data)
    return data

def convert_to_df(data, conditions, save=False):
    """
    Convert a 2D array of data into a DataFrame with a condition column.
    data: 2D array of data
    conditions: List of conditions
    """
    # Convert to a DataFrame for easy viewing
    df = pd.DataFrame(data, columns=["GSR_Truth", "GSR_Control", "GSR_Lie"])
    print(df.head())

    if save:
        df.to_csv('lie_detector_data.csv', index=False)
        print("Data saved to lie_detector_data.csv")

# Create simulated data for GSR
gsr_truth = simulate_responses(n_participants, mu=5, sigma=1)
gsr_control = simulate_responses(n_participants, mu=7, sigma=1.5)
gsr_lie = simulate_responses(n_participants, mu=10, sigma=2)

