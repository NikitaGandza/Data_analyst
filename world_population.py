import pandas as pd 

population_df = pd.read_csv('population.csv') #importing dataframe 

# instead of loading all data, we can inspect few first and last lines
# to print all lines: print(population_df)
print("First rows to inspect")
print(population_df.head())
print("Last rows to inspect")
print(population_df.tail())

# to check basic info(rows, columns, types)
print(population_df.info())