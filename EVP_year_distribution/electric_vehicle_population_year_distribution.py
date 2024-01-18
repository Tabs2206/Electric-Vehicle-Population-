# -*- coding: utf-8 -*-
"""Electric Vehicle Population Year Distribution.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nO91Vg5YMNbIitCTLhFUL3u44pF06Oq3

#Electric Vehicle Population Data
## Distribution of Electric Vehicles by Model Year

In this data we will found out the electric vehicles distribution based on the year

Import all the required liberary.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""#Reading the dataset
Dataset has been captured into a variable called 'dataset'. Later from the columns a new data set has been created to get the 'Model Year' and the 'Number of Vehicles' to get the distribution of model year by vechiles.
"""

dataset = pd.read_csv(r"C:\Users\tabs2\Downloads\Programming Assessment\data\Electric_Vehicle_Population_Data.csv")

#creating a new dataset for Model Year and the number of vehicles
year_distribution = dataset['Model Year'].value_counts().sort_index()

# Create a DataFrame from the new data
#year_distribution['Model Year'] = dataset['Model Year']

year_distribution

# Save the modified dataset to a new CSV file
year_distribution.to_csv('year_distribution.csv', index=False)

#plotting the bar chart

plt.figure(figsize=(12,6))
year_distribution.plot(kind = 'bar')
plt.title('Distribution of Electric Vehicles by Model Year')
plt.xlabel('Model Year')
plt.ylabel('Number of Vehicles')
plt.grid(axis = 'y')

# Save the plot as an image (e.g., PNG)
plt.savefig('electric_vehicles_by_model_year.png')
#show the plot
plt.show()