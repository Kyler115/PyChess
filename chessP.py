import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPalette, QColor
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
        
        for x in range(8):
            for y in range(8):
                button = QPushButton(f"{x},{y}")
                button.setCheckable(True)
                button.setBaseSize(100,100)
                
                if (x + y) % 2 == 0:
                    button.setStyleSheet("background-color: gray;")
                else:
                    button.setStyleSheet("background-color: white;")
                    
                    button.setStyleSheet(f"background-image: url('Users/kyler/OneDrive/Desktop/rook.png');")
                    layout.addWidget(button, x, y)
                    self.buttons.append(button)
                    
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
###############################################################################
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()