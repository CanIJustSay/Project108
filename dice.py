import random
import plotly.figure_factory as pff
diceData = []
for i in range(1,101):
    dice1 = int(random.randint(1,6))
    dice2 = int(random.randint(1,6))
    sum = dice1 + dice2
    diceData.append(sum)
graph = pff.create_distplot([diceData],["Graphing Dice"],show_hist=False)
graph.show()
