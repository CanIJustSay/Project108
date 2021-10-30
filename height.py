import pandas as pd
import plotly.figure_factory as pff


df = pd.read_csv("data.csv")

height = df["Height(Inches)"].tolist()
graph = pff.create_distplot([height],["Height"],show_hist=False)
graph.show()
