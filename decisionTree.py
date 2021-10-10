from node import Node
    

class DecisionTree:
    def __init__(self, heading, rows):
        self.heading = heading
        self.rootNode = self.main(rows, 0, "", None)


    # receives a single row and matches it with the question to see if it is true or false

    def askQuestion(self, row, question):
        if(question[1]=='=='):
            if(row[self.heading.index(question[0])] == question[2]):
                return True
            else:
                return False
        else:
            if(row[self.heading.index(question[0])] >= question[2]):
                return True
            else:
                return False


    # based on the question, it partitions the input rows into true rows and false rows

    def partition(self, rows, question):
        trueRows = []
        falseRows = []

        for row in rows:
            if(self.askQuestion(row, question)):
                trueRows.append(row)
            else:
                falseRows.append(row)
        return trueRows, falseRows


    # generates a question based on the type of the data in the column
    # note: the returned question will be compared to other generated questions and based on that
    #       an optimal question will be asked

    def generateQuestion(self, col,val):
        if(type(val) == int or type(val) == float):
            return (self.heading[col],">=",val)
        else:
            return (self.heading[col],"==",val)


    # generates a dictionary wherein the number of times a tuple appears is 
    # represented as {tuple : no. of appearance}. This is done for all unique tuples in the RESULT column

    def generateResultDict(self, rows):
        dict = {}
        for i in rows:
            if i[-1] not in dict:
                dict[i[-1]] = 1
            else:
                dict[i[-1]] += 1
        return dict

    # calculates the gini index of the rows

    def giniIndex(self, rows):
        dict = self.generateResultDict(rows)
        uncertainity = 1

        for i in dict:
            uncertainity -= (dict[i]/len(rows))**2

        return uncertainity

    # calculates the information gain

    def informationGain(self, left, right, gini):
        leftProbability = float(len(left)) / (len(left) + len(right))
        return gini - leftProbability * self.giniIndex(left) - (1 - leftProbability) * self.giniIndex(right)


    # tests all possible question for the particular level in the decision tree and splits the tree where
    # the information gain is the highest

    def bestSplit(self, rows):
        gini = self.giniIndex(rows)
        bestQuestion = ()
        bestInfoGain = 0

        for col in range(len(rows[0])-1):       #-1 to remove result column
            uniqueColVal = set([row[col] for row in rows])

            for val in uniqueColVal:
                question = self.generateQuestion(col,val)
                trueRows, falseRows = self.partition(rows, question)

                if len(trueRows) == 0 or len(falseRows) == 0:
                    continue

                infoGain = self.informationGain(trueRows, falseRows, gini)
                
                if(infoGain >= bestInfoGain):
                    bestInfoGain, bestQuestion = infoGain, question

        return bestInfoGain, bestQuestion 


    # returns the root node

    def getRoot(self):
        return self.rootNode

    # based on the best split, it divides the rows and then recursively generates nodes
    # for true and false rows       

    def main(self, rows, level, tf, parent):
        infoGain, question = self.bestSplit(rows)
        if(parent is None):
            parent = Node(question)

        node = Node(question)
        node.gain = infoGain
        if(tf=="True"):
            parent.left = node
        else:
            parent.right = node

        if(infoGain == 0):
            result = self.generateResultDict(rows)

            for i in result:
                result[i] = "{:.2f}".format((result[i]/len(rows)*100))+'%'
            node.answer = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))
            #print(level*"\t",tf)
            #print(level*"\t","leaf node",result)
            return

        trueRows, falseRows = self.partition(rows,question)

        #print(level*"\t",tf)
        #print(level*"\t","If "+question[0]+question[1]+str(question[2])+"?")


        self.main(trueRows, level+1, "True", node)

        self.main(falseRows, level+1, "False", node)
        
        return node


    
    


