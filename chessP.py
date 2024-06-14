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
    
    def getBID(self):
        return self.buttonId
###############################################################################
class MainWindow(QMainWindow):       
    
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle("bruh")
        layout = QGridLayout()
        self.buttons = []
        x,self.y,self.z = 0,0,0
        matrix = np.array([[1,2,3,4,5,3,2,1],[6,6,6,6,6,6,6,6],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[6,6,6,6,6,6,6,6],[1,2,3,4,5,3,2,1]])
        print(matrix)
        ##KEY##
        ## 1 = ROOKS
        ## 2 = KNIGHTS 
        ## 3 = BISHOPS
        ## 4 = QUEENS
        ## 5 = KINGS
        ## 6 = PAWNS
        ## 0 = EMPTY SPACE
        
        
        rookD = "rook.png"
        absPRD = QDir().absoluteFilePath(rookD)
        bishopD = "bishop.png"
        absPBD = QDir().absoluteFilePath(bishopD)
        knightD = "knight.png"
        absPKD = QDir().absoluteFilePath(knightD)
        kingD = "king.png"
        absPKKD = QDir().absoluteFilePath(kingD)
        queenD = "queen.png"
        absPQD = QDir().absoluteFilePath(queenD)
        pawnD = "pawn.png"
        absPPD = QDir().absoluteFilePath(pawnD)
        pawnW = "pawnW.png"
        absPPW = QDir().absoluteFilePath(pawnW)
        rookW = "rookW.png"
        absPRW = QDir().absoluteFilePath(rookW)
        knightW = "knightW.png"
        absPKW = QDir().absoluteFilePath(knightW)
        bishopW = "bishopW.png"
        absPBW = QDir().absoluteFilePath(bishopW)
        queenW = "queenW.png"
        absPQW = QDir().absoluteFilePath(queenW)
        kingW = "kingW.png"
        absPKKW = QDir().absoluteFilePath(kingW)
        
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
                    buttonT.setIcon(QIcon(absPRD))
                    buttonT.setIconSize(QSize(100,100))
                elif(self.z == 3):
                    buttonT.setIcon(QIcon(absPBD))
                    buttonT.setIconSize(QSize(100,100))
                elif(self.z == 2):
                    buttonT.setIcon(QIcon(absPKD))
                    buttonT.setIconSize(QSize(100,100))
                elif(self.z == 4):
                    buttonT.setIcon(QIcon(absPQD))
                    buttonT.setIconSize(QSize(100,100))
                elif(self.z == 5):
                    buttonT.setIcon(QIcon(absPKKD))
                    buttonT.setIconSize(QSize(100,100))
                elif(self.z == 6):
                    buttonT.setIcon(QIcon(absPBD))
                    buttonT.setIconSize(QSize(100,100))
                elif(self.z == 7):
                    buttonT.setIcon(QIcon(absPKD))
                    buttonT.setIconSize(QSize(100,100))  
                elif(self.z == 8):
                    buttonT.setIcon(QIcon(absPRD))
                    buttonT.setIconSize(QSize(100,100))
                elif(self.z in range(17)):
                    buttonT.setIcon(QIcon(absPPD))
                    buttonT.setIconSize(QSize(100,100))
                elif(self.z >= 49 and self.z in range(57)):
                    buttonT.setIcon(QIcon(absPPW))
                    buttonT.setIconSize(QSize(100,100))
                elif(self.z == 57 or self.z == 64):
                    buttonT.setIcon(QIcon(absPRW))
                    buttonT.setIconSize(QSize(100,100))
                elif(self.z == 58 or self.z == 63):
                    buttonT.setIcon(QIcon(absPKW))
                    buttonT.setIconSize(QSize(100,100))
                elif(self.z == 59 or self.z == 62):
                    buttonT.setIcon(QIcon(absPBW))
                    buttonT.setIconSize(QSize(100,100))      
                elif(self.z == 60):
                    buttonT.setIcon(QIcon(absPQW))
                    buttonT.setIconSize(QSize(100,100)) 
                elif(self.z == 61):
                    buttonT.setIcon(QIcon(absPKKW))
                    buttonT.setIconSize(QSize(100,100)) 

    
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
    def bClick(self):
        button = self.sender()
        buttonId = button.getBID()
        print(f"Button {buttonId} clicked.")
        
###############################################################################
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()