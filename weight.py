import plotly.express as px
import plotly.figure_factory as ff
import csv
import pandas as pd

weight = pd.read_csv("data.csv")
fig = ff.create_distplot([weight["Weight"]],["Weight"],show_hist = False)
fig.show()