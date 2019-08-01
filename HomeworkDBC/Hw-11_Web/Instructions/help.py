import pandas as pd

data = "Resources/cities.csv"
data_input = pd.read_csv(data, low_memory=False)
print(data_input)

data_input.to_html("cities_table.html")

