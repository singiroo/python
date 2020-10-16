import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("tetris.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    
    msg = True
    
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.block2D = []
        self.stack2D = []
        self.scrin2D = []
        self.lbl2D = []
        
        self.initBlock2Dstack2Dscrin2D()
        
        self.print2D(self.block2D)
        print()
        self.print2D(self.stack2D)
        print()
        self.print2D(self.scrin2D)
        
        self.scrin2D[0][0] = 1
        self.scrin2D[0][1] = 1
        self.scrin2D[1][1] = 1
        self.scrin2D[2][1] = 1
        
        self.print2D(self.scrin2D)
        
        
        for i in range(len(self.scrin2D)):
            arr = []
            for j in range(len(self.scrin2D[i])):
                pb = QLabel('', self)
                pb.setGeometry(40 * j, 40*i, 40 , 40)
                pb.setStyleSheet("background-color : darkgray; border : 1px solid black")
                arr.append(pb)
            self.lbl2D.append(arr)
        
            
        self.myRender()
        self.print2D(self.lbl2D)
        
        
        
        
    
    def initBlock2Dstack2Dscrin2D(self):
        for i in range(20):
            arr = []
            for j in range(10):
               arr.insert(j, 0)
            self.block2D.append(arr)
            self.stack2D.append(arr)
            self.scrin2D.append(arr)
            
            
            
    def print2D(self,list):
        print("===============================print2D")
        for i in range(20):
            for j in range(10):
                print(list[i][j], end=" ")
        
            print()
        print("===============================print2D")
    
    
    def myRender(self):
        for i in range(len(self.scrin2D)):
            for j in range(len(self.scrin2D[i])):
                if self.scrin2D[i][j] == 0:
                    self.lbl2D[i][j].setStyleSheet("background-color : darkgray; border : 1px solid black")
                if self.scrin2D[i][j] == 1:
                    self.lbl2D[i][j].setStyleSheet("background-color : red; border : 1px solid black")
                if self.scrin2D[i][j] == 2:
                    self.lbl2D[i][j].setStyleSheet("background-color : orange; border : 1px solid black")
                if self.scrin2D[i][j] == 3:
                    self.lbl2D[i][j].setStyleSheet("background-color : yellow; border : 1px solid black")
                if self.scrin2D[i][j] == 4:
                    self.lbl2D[i][j].setStyleSheet("background-color : green; border : 1px solid black")
                if self.scrin2D[i][j] == 5:
                    self.lbl2D[i][j].setStyleSheet("background-color : blue; border : 1px solid black")
                if self.scrin2D[i][j] == 6:
                    self.lbl2D[i][j].setStyleSheet("background-color : navy; border : 1px solid black")
                if self.scrin2D[i][j] == 7:
                    self.lbl2D[i][j].setStyleSheet("background-color : violet; border : 1px solid black")
                
                if self.scrin2D[i][j] == 11:
                    self.lbl2D[i][j].setStyleSheet("background-color : red; border : 1px solid black")
                if self.scrin2D[i][j] == 12:
                    self.lbl2D[i][j].setStyleSheet("background-color : orange; border : 1px solid black")
                if self.scrin2D[i][j] == 13:
                    self.lbl2D[i][j].setStyleSheet("background-color : yellow; border : 1px solid black")
                if self.scrin2D[i][j] == 14:
                    self.lbl2D[i][j].setStyleSheet("background-color : green; border : 1px solid black")
                if self.scrin2D[i][j] == 15:
                    self.lbl2D[i][j].setStyleSheet("background-color : blue; border : 1px solid black")
                if self.scrin2D[i][j] == 16:
                    self.lbl2D[i][j].setStyleSheet("background-color : navy; border : 1px solid black")
                if self.scrin2D[i][j] == 17:
                    self.lbl2D[i][j].setStyleSheet("background-color : violet; border : 1px solid black")
                
                    
                
#         self.pushButton.clicked.connect(self.changeMsg)


  
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()