import pygame
import math

class Visualize:
    def __init__(self, node):
        self.width=1300
        self.height=700
        self.fontsize = 16
        self.backgroundColor = (255,255,255)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 128)
        self.red = (255,0,0)
        self.lineColor = (0,0,0)
        self.screen = None
        self.node = node
        self.angle = 150
        self.length = 200


    def print(self):
        self.printNode(self.node,0,"ROOT")

    def printNode(self, node, level, branch):
        indent = level*"\t"
        if(node.gain==0):
            print(indent,branch)
            for key, value in node.answer.items():
                print(indent, key,"(",value,")")
            print()
            #print(level*"\t",node.gain)
        else:
            print(indent,branch)
            print(indent,"IS",node.question[0],node.question[1],str(node.question[2]),"?")
            print()
            #print(level*"\t",node.gain)
        if node.left is not None:
            self.printNode(node.left, level+1, "TRUE")
        if node.right is not None:
            self.printNode(node.right, level+1, "FALSE")
    
    def draw(self):
        pygame.init()
        self.screen=pygame.display.set_mode((self.width,self.height),pygame.RESIZABLE)
        self.screen.fill(self.backgroundColor)

        self.font = pygame.font.Font('freesansbold.ttf', self.fontsize)

        self.drawNode(self.node, self.width//2, 30, self.length, self.angle)
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    def trig(self,angle,to,length):
        x=math.cos(angle)*(length)+to[0]
        y=math.sin(angle)*(length)+to[1]
        return([x,y])

    def drawNode(self, node, x, y, length, angle):
        displayText = ""
        if node.gain == 0:
            for key, value in node.answer.items():
                displayText += (key+ "("+ value+")")
                text = self.font.render(displayText, True, self.green, self.blue)
                
        else:
            displayText += ("IS "+node.question[0]+node.question[1]+str(node.question[2])+"?")
            text = self.font.render(displayText, True, self.green, self.red)
                
        textRect = text.get_rect()
        textRect.center = (x, y)

        angleTrim=math.radians(90)

        langle = angleTrim - math.radians(angle//2)
        rangle = angleTrim + math.radians(angle//2)
        oldXY = [x,y]

        newXY = self.trig(langle, oldXY, length) 

        if node.left is not None:
            pygame.draw.line(self.screen,self.green,oldXY,newXY,1)
            self.drawNode(node.left, newXY[0], newXY[1], length, angle*0.85)


        newXY = self.trig(rangle, oldXY, length)
        if node.right is not None:
            pygame.draw.line(self.screen,self.red,oldXY,newXY,1)
            self.drawNode(node.right, newXY[0], newXY[1], length*0.8, angle*0.85)
        
        self.screen.blit(text, textRect)

        pygame.display.update()

        