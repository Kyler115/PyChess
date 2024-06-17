import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget
from PyQt5.QtCore import QSize, Qt, QDir
from PyQt5.QtGui import QPalette, QColor, QIcon
###############################################################################
class Color(QWidget): 
    
    def __init__(self,color):
        super().__init__()
        self.setAutoFillBackground(True)
        
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)
###############################################################################
class Button(QPushButton):
    def __init__(self,buttonId):
        super().__init__()      
        self.buttonId = buttonId 
        self.typeB = ""
    
    def getBID(self):
        return self.buttonId
    
    def setBID(self,iD):
        self.buttonId = iD
        
    def setType(self,typeB):
        self.typeB = typeB
        
    def getType(self):
        return self.typeB
###############################################################################
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle("Chesssssssssssssssse")
        layout = QGridLayout()
        self.buttons = []
        self.flag = False
        self.stack = []
        self.prevButt = ""
        x,self.y,self.z = 0,0,0
        ## matrix = np.array([[1,2,3,4,5,3,2,1],[6,6,6,6,6,6,6,6],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[6,6,6,6,6,6,6,6],[1,2,3,4,5,3,2,1]])
        ##print(matrix)
        ##KEY##
        ## 1 = ROOKS
        ## 2 = KNIGHTS 
        ## 3 = BISHOPS
        ## 4 = QUEENS
        ## 5 = KINGS
        ## 6 = PAWNS
        ## 0 = EMPTY SPACE
        
        
        rookD = "rook.png"
        self.absPRD = QDir().absoluteFilePath(rookD)
        bishopD = "bishop.png"
        self.absPBD = QDir().absoluteFilePath(bishopD)
        knightD = "knight.png"
        self.absPKD = QDir().absoluteFilePath(knightD)
        kingD = "king.png"
        self.absPKKD = QDir().absoluteFilePath(kingD)
        queenD = "queen.png"
        self.absPQD = QDir().absoluteFilePath(queenD)
        pawnD = "pawn.png"
        self.absPPD = QDir().absoluteFilePath(pawnD)
        pawnW = "pawnW.png"
        self.absPPW = QDir().absoluteFilePath(pawnW)
        rookW = "rookW.png"
        self.absPRW = QDir().absoluteFilePath(rookW)
        knightW = "knightW.png"
        self.absPKW = QDir().absoluteFilePath(knightW)
        bishopW = "bishopW.png"
        self.absPBW = QDir().absoluteFilePath(bishopW)
        queenW = "queenW.png"
        self.absPQW = QDir().absoluteFilePath(queenW)
        kingW = "kingW.png"
        self.absPKKW = QDir().absoluteFilePath(kingW)
        
        for x in range(8):
            for y in range(8):
                buttonT = Button(self.z)
                buttonT.setMinimumSize(100,100)
                buttonT.setMaximumSize(100,100)
                buttonT.clicked.connect(self.bClick)

                if (x + y) % 2 == 0:
                    buttonT.setStyleSheet("background-color: white;")
                    layout.addWidget(buttonT, x, y)
                    self.buttons.append(buttonT)
                    self.z = self.z+1
                else:
                    buttonT.setStyleSheet("background-color: grey;")
                    layout.addWidget(buttonT, x, y)
                    self.buttons.append(buttonT)
                    self.z = self.z+1
                    
                if(self.z == 1):
                    buttonT.setIcon(QIcon(self.absPRD))
                    buttonT.setIconSize(QSize(100,100))
                    buttonT.setBID(self.z)
                    buttonT.setType("rook")
                elif(self.z == 3):
                    buttonT.setIcon(QIcon(self.absPBD))
                    buttonT.setIconSize(QSize(100,100))
                    buttonT.setBID(self.z)
                    buttonT.setType("bishop")
                elif(self.z == 2):
                    buttonT.setIcon(QIcon(self.absPKD))
                    buttonT.setIconSize(QSize(100,100))
                    buttonT.setBID(self.z)
                    buttonT.setType("knight")
                elif(self.z == 4):
                    buttonT.setIcon(QIcon(self.absPQD))
                    buttonT.setIconSize(QSize(100,100))
                    buttonT.setBID(self.z)
                    buttonT.setType("queen")
                elif(self.z == 5):
                    buttonT.setIcon(QIcon(self.absPKKD))
                    buttonT.setIconSize(QSize(100,100))
                    buttonT.setBID(self.z)
                    buttonT.setType("king")
                elif(self.z == 6):
                    buttonT.setIcon(QIcon(self.absPBD))
                    buttonT.setIconSize(QSize(100,100))
                    buttonT.setBID(self.z)
                    buttonT.setType("bishop")
                elif(self.z == 7):
                    buttonT.setIcon(QIcon(self.absPKD))
                    buttonT.setIconSize(QSize(100,100))  
                    buttonT.setBID(self.z)
                    buttonT.setType("knight")
                elif(self.z == 8):
                    buttonT.setIcon(QIcon(self.absPRD))
                    buttonT.setIconSize(QSize(100,100))
                    buttonT.setBID(self.z)
                    buttonT.setType("rook")
                elif(self.z in range(17)):
                    buttonT.setIcon(QIcon(self.absPPD))
                    buttonT.setIconSize(QSize(100,100))
                    buttonT.setBID(self.z)
                    buttonT.setType("pawn")
                elif(self.z < 49):
                    buttonT.setIconSize(QSize(100,100))
                    buttonT.setBID(self.z)
                elif(self.z >= 49 and self.z in range(57)):
                    buttonT.setIcon(QIcon(self.absPPW))
                    buttonT.setIconSize(QSize(100,100))
                    buttonT.setBID(self.z)
                    buttonT.setType("pawn")
                elif(self.z == 57 or self.z == 64):
                    buttonT.setIcon(QIcon(self.absPRW))
                    buttonT.setIconSize(QSize(100,100))
                    buttonT.setBID(self.z)
                    buttonT.setType("rook")
                elif(self.z == 58 or self.z == 63):
                    buttonT.setIcon(QIcon(self.absPKW))
                    buttonT.setIconSize(QSize(100,100))
                    buttonT.setBID(self.z)
                    buttonT.setType("knight")
                elif(self.z == 59 or self.z == 62):
                    buttonT.setIcon(QIcon(self.absPBW))
                    buttonT.setIconSize(QSize(100,100))  
                    buttonT.setBID(self.z)
                    buttonT.setType("bishop")
                elif(self.z == 60):
                    buttonT.setIcon(QIcon(self.absPQW))
                    buttonT.setIconSize(QSize(100,100)) 
                    buttonT.setBID(self.z)
                    buttonT.setType("queen")
                elif(self.z == 61):
                    buttonT.setIcon(QIcon(self.absPKKW))
                    buttonT.setIconSize(QSize(100,100)) 
                    buttonT.setBID(self.z)
                    buttonT.setType("king")

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
    def bClick(self):
        button = self.sender()
        buttonId = button.getBID()
        buttonType = button.getType()
        if(self.flag == True):
            if(buttonId == self.stack[-1].getBID()+8 or 
               buttonId == self.stack[-1].getBID()+9 or 
               buttonId == self.stack[-1].getBID()+7):
                button.setIcon(QIcon(self.absPPD))  
                self.stack.pop().setIcon(QIcon())
                self.flag = False
                button.setType(self.prevButt.getType())
        if(buttonType == "pawn" ):
            self.flag = True
            self.stack.append(button)
            self.prevButt = button
        elif(buttonType == ""):
            print("bruh")

        
###############################################################################
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()