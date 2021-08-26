import pandas as pd
import plotly_express as px

df = pd.read_csv("CovidData.csv")
fig = px.scatter(df, x = 'date',y = 'cases',color = 'country', size_max = '60') 
fig.show()