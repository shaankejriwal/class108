import random
import plotly.express as px
import plotly.figure_factory as ff
import csv
import pandas as pd

final = pd.read_csv("data.csv")
fig = ff.create_distplot([final["Height"].tolist()],['Height'],show_hist = False)
fig.show()