import numpy as np
import pandas as pd

class LieDetectorSimulator:
    def __init__(self, num_participants):
        self.num_participants = num_participants
        self.conditions = ['lie', 'truth', 'neutral']
        self.measurements = ['heart_rate', 'gsr', 'pupil_diameter', 'respiration_rate']
        self.data = self._generate_data()

    def _generate_data(self):
        data = {}
        for condition in self.conditions:
            for measurement in self.measurements:
                column_name = f"{measurement}_{condition}"
                data[column_name] = self._simulate_measurement(condition)
        return pd.DataFrame(data)

    def _simulate_measurement(self, condition): 
        if condition == 'lie':
            return np.random.normal(loc=80, scale=10, size=self.num_participants)
        elif condition == 'truth':
            return np.random.normal(loc=70, scale=10, size=self.num_participants)
        else:  # neutral
            return np.random.normal(loc=75, scale=10, size=self.num_participants)

    def get_data(self):
        return self.data

if __name__ == "__main__":
    # Example usage:
    simulator = LieDetectorSimulator(num_participants=100)
    data = simulator.get_data()
    print(data.head())