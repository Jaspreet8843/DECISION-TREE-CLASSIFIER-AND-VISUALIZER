from decisionTree import DecisionTree
from visualize import Visualize
import pandas as pd


file = pd.read_csv('dataset/iris.csv')

heading = file.keys().tolist()
rows = file.values.tolist()
dt = DecisionTree(heading, rows, 0.75)

dt.calcAccuracy()
root = dt.getRoot()

v = Visualize(root)

#v.draw()

#v.print()


