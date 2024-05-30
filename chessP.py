import sys
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
class MainWindow(QMainWindow):        
    def bClick(self, z):
            print(z)
            
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle("bruh")
        layout = QGridLayout()
        self.buttons = []
        x,self.y,self.z = 0,0,0
        
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
                button = QPushButton()
                button.setMinimumSize(100,100)
                button.setMaximumSize(100,100)
                button.clicked.connect(self.bClick)
                button.setCheckable(True)

                if (x + y) % 2 == 0:
                    button.setStyleSheet("background-color: white;")
                    layout.addWidget(button, x, y)
                    self.buttons.append(button)
                    self.z = self.z+1
                else:
                    button.setStyleSheet("background-color: grey;")
                    layout.addWidget(button, x, y)
                    self.buttons.append(button)
                    self.z = self.z+1
                if(self.z == 1):
                    button.setIcon(QIcon(absPRD))
                    button.setIconSize(QSize(100,100))
                elif(self.z == 3):
                    button.setIcon(QIcon(absPBD))
                    button.setIconSize(QSize(100,100))
                elif(self.z == 2):
                    button.setIcon(QIcon(absPKD))
                    button.setIconSize(QSize(100,100))
                elif(self.z == 4):
                    button.setIcon(QIcon(absPQD))
                    button.setIconSize(QSize(100,100))
                elif(self.z == 5):
                    button.setIcon(QIcon(absPKKD))
                    button.setIconSize(QSize(100,100))
                elif(self.z == 6):
                    button.setIcon(QIcon(absPBD))
                    button.setIconSize(QSize(100,100))
                elif(self.z == 7):
                    button.setIcon(QIcon(absPKD))
                    button.setIconSize(QSize(100,100))    
                elif(self.z == 8):
                    button.setIcon(QIcon(absPRD))
                    button.setIconSize(QSize(100,100))
                elif(self.z in range(17)):
                    button.setIcon(QIcon(absPPD))
                    button.setIconSize(QSize(100,100))                    
                elif(self.z >= 49 and self.z in range(57)):
                    button.setIcon(QIcon(absPPW))
                    button.setIconSize(QSize(100,100))
                elif(self.z == 57 or self.z == 64):
                    button.setIcon(QIcon(absPRW))
                    button.setIconSize(QSize(100,100))
                elif(self.z == 58 or self.z == 63):
                    button.setIcon(QIcon(absPKW))
                    button.setIconSize(QSize(100,100))
                elif(self.z == 59 or self.z == 62):
                    button.setIcon(QIcon(absPBW))
                    button.setIconSize(QSize(100,100))      
                elif(self.z == 60):
                    button.setIcon(QIcon(absPQW))
                    button.setIconSize(QSize(100,100)) 
                elif(self.z == 61):
                    button.setIcon(QIcon(absPKKW))
                    button.setIconSize(QSize(100,100)) 
    
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
###############################################################################
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()