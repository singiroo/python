import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt
from random import randint
import random


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("tetris.ui")[0]

class Block():
    
    def __init__(self, kinds):
        self.kind = kinds;
        self.status = 1;
        self.i = 1;
        self.j = 5;
 
    
    def __str__(self):
        return "[ kind : %d, status : %d, i : %d, j : %d ]" %(self.kind, self.status, self.i, self.j)




#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :

    
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.block2D = []
        self.stack2D = []
        self.scrin2D = []
        self.lbl2D = []
        
        self.initBlock2Dstack2Dscrin2D()
        
        self.block = Block(4);        
        
        self.flagCollision = False;
        
        self.print2D(self.block2D)
        print()
        self.print2D(self.stack2D)
        print()
        self.print2D(self.scrin2D)
        
#         self.scrin2D[0][0] = 1
#         self.scrin2D[0][1] = 1
#         self.scrin2D[1][1] = 1
#         self.scrin2D[2][1] = 1 
        
        
        
        for i in range(len(self.scrin2D)):
            arr = []
            for j in range(len(self.scrin2D[i])):
                pb = QLabel('', self)
                pb.setGeometry(40 * j, 40*i, 40 , 40)
                pb.setStyleSheet("background-color : darkgray; border : 1px solid black")
                arr.append(pb)
            self.lbl2D.append(arr)
        
            
        print(self.block)
    
    
    
    def changeBlockStatus(self):
        if self.block.kind == 1:
            self.block.status = 1;
        
        if self.block.kind == 2 or self.block.kind == 3 or self.block.kind == 4:
            if self.block.status == 1:
                self.block.status = 2;
            elif self.block.status == 2 :
                self.block.status = 1;
            
        
        if self.block.kind == 5 or self.block.kind == 6 or self.block.kind == 7:
            if self.block.status == 1:
                self.block.status = 2;
            elif self.block.status == 2:
                self.block.status = 3;
            elif self.block.status == 3:
                self.block.status = 4;
            elif self.block.status == 4:
                self.block.status = 1;
            
            
    ## block2D 와 stack2D의 정보를 scrin2D로 옮김
    def moveStackBlockToScrin(self):
        for i in range(20):
            for j in range(10):
                self.scrin2D[i][j] = self.stack2D[i][j] + self.block2D[i][j]
                
        
    ## block2D에 블록 정보를 입력
    def setBlock2DWithBlock(self):
        
        for i in range(20):
            for j in range(10):
                self.block2D[i][j] = 0
        
        if self.block.kind == 1:
            self.block2D[self.block.i][self.block.j] = self.block.kind
            self.block2D[self.block.i+1][self.block.j] = self.block.kind
            self.block2D[self.block.i+1][self.block.j+1] = self.block.kind
            self.block2D[self.block.i][self.block.j+1] = self.block.kind
            
        if self.block.kind == 2:
            if self.block.status == 1: 
                self.block2D[self.block.i-1][self.block.j] = self.block.kind;
                self.block2D[self.block.i][self.block.j] = self.block.kind;
                self.block2D[self.block.i+1][self.block.j] = self.block.kind;
                self.block2D[self.block.i+2][self.block.j] = self.block.kind;
            
            if self.block.status == 2:
                self.block2D[self.block.i][self.block.j-2] = self.block.kind;
                self.block2D[self.block.i][self.block.j-1] = self.block.kind;
                self.block2D[self.block.i][self.block.j] = self.block.kind;
                self.block2D[self.block.i][self.block.j+1] = self.block.kind;
       
        
        if self.block.kind == 3:
            if self.block.status == 1:
                self.block2D[self.block.i][self.block.j-1]=self.block.kind;
                self.block2D[self.block.i][self.block.j]=self.block.kind;
                self.block2D[self.block.i+1][self.block.j]=self.block.kind;
                self.block2D[self.block.i+1][self.block.j+1]=self.block.kind;

            if self.block.status == 2:
                self.block2D[self.block.i-1][self.block.j]=self.block.kind;
                self.block2D[self.block.i][self.block.j]=self.block.kind;
                self.block2D[self.block.i][self.block.j-1]=self.block.kind;
                self.block2D[self.block.i+1][self.block.j-1]=self.block.kind;
 
        if self.block.kind == 4: 
            if self.block.status == 1: 
                self.block2D[self.block.i][self.block.j+1]=self.block.kind;
                self.block2D[self.block.i][self.block.j]=self.block.kind;
                self.block2D[self.block.i+1][self.block.j]=self.block.kind;
                self.block2D[self.block.i+1][self.block.j-1]=self.block.kind;

            if self.block.status == 2:
                self.block2D[self.block.i-1][self.block.j-1]=self.block.kind;
                self.block2D[self.block.i][self.block.j-1]=self.block.kind;
                self.block2D[self.block.i][self.block.j]=self.block.kind;
                self.block2D[self.block.i+1][self.block.j]=self.block.kind;
        
        if self.block.kind == 5:
            if self.block.status == 1: 
                self.block2D[self.block.i][self.block.j-1] = self.block.kind;
                self.block2D[self.block.i][self.block.j] = self.block.kind;
                self.block2D[self.block.i-1][self.block.j] = self.block.kind;
                self.block2D[self.block.i][self.block.j+1] = self.block.kind;

            if self.block.status == 2:  
                self.block2D[self.block.i-1][self.block.j] = self.block.kind;
                self.block2D[self.block.i][self.block.j] = self.block.kind;
                self.block2D[self.block.i+1][self.block.j] = self.block.kind;
                self.block2D[self.block.i][self.block.j+1] = self.block.kind;
             
            if self.block.status == 3:  
                self.block2D[self.block.i][self.block.j-1] = self.block.kind;
                self.block2D[self.block.i][self.block.j] = self.block.kind;
                self.block2D[self.block.i][self.block.j+1] = self.block.kind;
                self.block2D[self.block.i+1][self.block.j] = self.block.kind;
             
            if self.block.status == 4:  
                self.block2D[self.block.i-1][self.block.j] = self.block.kind;
                self.block2D[self.block.i][self.block.j] = self.block.kind;
                self.block2D[self.block.i+1][self.block.j] = self.block.kind;
                self.block2D[self.block.i][self.block.j-1] = self.block.kind;
             
         
        
        if self.block.kind == 6:  
            if self.block.status == 1:  
                self.block2D[self.block.i-1][self.block.j] = self.block.kind;
                self.block2D[self.block.i][self.block.j] = self.block.kind;
                self.block2D[self.block.i+1][self.block.j] = self.block.kind;
                self.block2D[self.block.i-1][self.block.j-1] = self.block.kind;
             
            if self.block.status == 2:  
                self.block2D[self.block.i][self.block.j-1] = self.block.kind;
                self.block2D[self.block.i][self.block.j] = self.block.kind;
                self.block2D[self.block.i][self.block.j+1] = self.block.kind;
                self.block2D[self.block.i-1][self.block.j+1] = self.block.kind;
             
            if self.block.status == 3:  
                self.block2D[self.block.i-1][self.block.j] = self.block.kind;
                self.block2D[self.block.i][self.block.j] = self.block.kind;
                self.block2D[self.block.i+1][self.block.j] = self.block.kind;
                self.block2D[self.block.i+1][self.block.j+1] = self.block.kind;
             
            if self.block.status == 4:  
                self.block2D[self.block.i][self.block.j-1] = self.block.kind;
                self.block2D[self.block.i][self.block.j] = self.block.kind;
                self.block2D[self.block.i][self.block.j+1] = self.block.kind;
                self.block2D[self.block.i+1][self.block.j-1] = self.block.kind;
             
         
        
        if self.block.kind == 7:  
            if self.block.status == 1:  
                self.block2D[self.block.i-1][self.block.j] = self.block.kind;
                self.block2D[self.block.i][self.block.j] = self.block.kind;
                self.block2D[self.block.i+1][self.block.j] = self.block.kind;
                self.block2D[self.block.i+1][self.block.j-1] = self.block.kind;                
             
            if self.block.status == 2:  
                self.block2D[self.block.i-1][self.block.j-1] = self.block.kind;
                self.block2D[self.block.i][self.block.j-1] = self.block.kind;
                self.block2D[self.block.i][self.block.j] = self.block.kind;
                self.block2D[self.block.i][self.block.j+1] = self.block.kind;
             
            if self.block.status == 3:  
                self.block2D[self.block.i-1][self.block.j+1] = self.block.kind;
                self.block2D[self.block.i-1][self.block.j] = self.block.kind;
                self.block2D[self.block.i][self.block.j] = self.block.kind;
                self.block2D[self.block.i+1][self.block.j] = self.block.kind;
                
             
            if self.block.status == 4:  
                self.block2D[self.block.i][self.block.j-1] = self.block.kind;
                self.block2D[self.block.i][self.block.j] = self.block.kind;
                self.block2D[self.block.i][self.block.j+1] = self.block.kind;
                self.block2D[self.block.i+1][self.block.j+1] = self.block.kind;    
    
    
    
    
    def collisionTest(self):
        for i in range(20):
            if self.block2D[i][0] > 0:
                self.flagCollision = True
                break;
    
         

    def keyPressEvent(self, e):
        
        self.flagCollision = False
        
        itemp = self.block.i
        jtemp = self.block.j
        status = self.block.status
        
        if e.key() == Qt.Key_Down:
            print("down")
            self.block.i += 1
        
        if e.key() == Qt.Key_Up:
            print("up")
#             self.block.i -= 1
            self.changeBlockStatus()
        
        if e.key() == Qt.Key_Left:
            print("left")            
            
            self.collisionTest()
            
            if not self.flagCollision:
                self.block.j -= 1
        
        if e.key() == Qt.Key_Right:
           
            print("right")
            
            self.block.j += 1
        
        
#         print(self.flagCollision)
#         print("========================before")
#         print("block2D")
#         self.print2D(self.block2D)
#         print("stacck2D")
#         self.print2D(self.stack2D)
#         print("scrin2D")
#         self.print2D(self.scrin2D)
#         
        try:
            self.setBlock2DWithBlock()
            self.moveStackBlockToScrin()
            self.myRender()
        except:
            print("예외 발생!")
            self.block.i = itemp
            self.block.j = jtemp
            self.block.status = status
        
        
       
        
#         print("=========================after")
#         print("block2D")
#         self.print2D(self.block2D)
#         print("stacck2D")
#         self.print2D(self.stack2D)
#         print("scrin2D")
#         self.print2D(self.scrin2D)
        
        
        
        print(self.block)    
        
        
        
    # block2D, stack2D, scrint2D  리스트 초기화
    def initBlock2Dstack2Dscrin2D(self):
        for i in range(20):
            self.block2D.append([0,0,0,0,0, 0,0,0,0,0])
            self.stack2D.append([0,0,0,0,0, 0,0,0,0,0])
            self.scrin2D.append([0,0,0,0,0, 0,0,0,0,0])
            
            
    #인자로 전한 리스트를 출력        
    def print2D(self,list):
        print("===============================print2D")
        for i in range(20):
            for j in range(10):
                print(list[i][j], end=" ")
        
            print()
        print("===============================print2D")
    
    # scrin2D 정보를 가지고 lbl2D에 색깔 칠하기
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