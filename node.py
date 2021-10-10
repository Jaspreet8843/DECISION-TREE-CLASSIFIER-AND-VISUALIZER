# represents a node in the decision tree

class Node:
    def __init__(self, question):
        self.left = None
        self.right = None
        self.question = question
        self.gain = None
        self.answer = {}