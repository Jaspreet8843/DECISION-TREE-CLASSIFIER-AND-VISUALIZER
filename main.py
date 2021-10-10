from decisionTree import DecisionTree
from visualize import Visualize
import pandas as pd


file = pd.read_csv('dataset/dataset.csv')

heading = file.keys().tolist()
rows = file.values.tolist()

dt = DecisionTree(heading, rows)

root = dt.getRoot()

Visualize(root)


