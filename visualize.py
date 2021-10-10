
class Visualize:
    def __init__(self, node):
        self.printNode(node,0,"ROOT")

    def printNode(self, node, level, branch):
        indent = level*"\t"
        if(node.gain==0):
            print(indent,branch)
            for key, value in node.answer.items():
                print(indent, key,"( probability: ",value,")")
            print()
            #print(level*"\t",node.gain)
        else:
            print(indent,branch)
            print(indent,"IS",node.question[0],node.question[1],node.question[2],"?")
            print()
            #print(level*"\t",node.gain)
        if node.left is not None:
            self.printNode(node.left, level+1, "TRUE")
        if node.right is not None:
            self.printNode(node.right, level+1, "FALSE")