import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtCore import Qt
from random import randint
import random
import threading
import time
from PyQt5.QtGui import QIcon


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("tetris.ui")[0]

class Block():
    
    def __init__(self, kinds):
        self.kind = kinds;
        self.status = 1;
        self.i = 1;
        self.j = 5;
    
    
    
    def myinit(self):
        self.kind = 1
        self.status = 1
        self.i = 1
        self.j = 5
    
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
        self.flagIng = True
        self.initBlock2Dstack2Dscrin2D()
        
        self.block = Block(4);        
        
        self.print2D(self.block2D)
        print()
        self.print2D(self.stack2D)
        print()
        self.print2D(self.scrin2D)
        
#         self.scrin2D[0][0] = 1
#         self.scrin2D[0][1] = 1
#         self.scrin2D[1][1] = 1
#         self.scrin2D[2][1] = 1 
        
        self.stack2D[19][0] = 12
        self.stack2D[19][1] = 12
        self.stack2D[19][2] = 12
        self.stack2D[19][3] = 12
        
        self.icon = QtGui.QIcon("white.jpg")
        self.icon1 = QtGui.QIcon("red.jpg")
        self.icon2 = QtGui.QIcon("green.jpg")
        
        
        
        self.lblCnt.setText(str(1))
        
        for i in range(len(self.scrin2D)):
            arr = []
            for j in range(len(self.scrin2D[i])):
#                 pb = QLabel('', self)
                pb = QPushButton('', self)
                pb.setGeometry(29 * j, 29*i, 30 , 30)
                pb.setIconSize(QtCore.QSize(30 , 30))
                pb.setIcon(QIcon(self.icon))
#                 pb.setStyleSheet("background-color : darkgray; border : 1px solid black")
                arr.append(pb)
            self.lbl2D.append(arr)
        
            
        print(self.block)
    
    
    
    def downThread(self, start, stop):
        for i in range(start, stop):
            time.sleep(5)
            self.realPress(Qt.Key_Down)
    
    
    
     
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
    
    
    
    
    def collisionTest(self, flag):
        for i in range(20):
            if self.block2D[i][0] > 0:
                flag = True
                break;
    
    def isCollision(self):
        
        for i in range(20):
            for j in range(10):
                if self.stack2D[i][j] > 0 and self.block2D[i][j] > 0:
                    return True
        return False
    
    def realPress(self, key):
        
        if not self.flagIng:
            QMessageBox.warning(self, "게임종료", '게임이 종료되었습니다.')
            return
        
        
        flagColBound = False
        flagDown = False
        pre_i = self.block.i
        pre_j = self.block.j
        
        pre_status = self.block.status
        
        if key == Qt.Key_S:
            print("down")
            self.block.i += 1
            flagDown = True
        
        if key == Qt.Key_W:
            print("up")
#             self.block.i -= 1
            self.changeBlockStatus()
        
        if key == Qt.Key_A:
            print("left")            
            self.block.j -= 1
            
#             self.collisionTest(flagCollision)
#             
#             if not self.flagCollision:
        
        if key == Qt.Key_D:
           
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
#         try:
#             self.block.j = self.block.j - 10
#             self.setBlock2DWithBlock()
# #             self.moveStackBlockToScrin()
# #             self.myRender()
#             self.block.j = self.block.j + 10
#             self.setBlock2DWithBlock()
#         except:
#             print("예외 발생!")
#             flagColBound = True    
#         
#         self.moveStackBlockToScrin()
#         
#         flagCollision  = self.isCollision()
#         
#             
#         if  flagColBound or flagCollision :    
#             self.block.i = pre_i
#             self.block.j = pre_j
#             self.block.status = pre_status
#             self.setBlock2DWithBlock()
#             self.moveStackBlockToScrin()
#         
#         
#         self.myRender()
#        
        
#         print("=========================after")
#         print("block2D")
#         self.print2D(self.block2D)
#         print("stacck2D")
#         self.print2D(self.stack2D)
#         print("scrin2D")
#         self.print2D(self.scrin2D)
        
        
        
        print(self.block)    
        
        try:
            self.block.j = self.block.j - 10
            self.setBlock2DWithBlock()
            self.block.j = self.block.j + 10
            self.setBlock2DWithBlock()
        except:    
            print('예외가 발생했습니다.')
            flagColBound = True
            
        flag_collision = self.isCollision()  
        
        print("flag_collision", flag_collision)
        
        if flagColBound or flag_collision :
            self.block.status = pre_status;
            self.block.i = pre_i;
            self.block.j = pre_j;
            
            self.setBlock2DWithBlock();
            self.moveStackBlockToScrin();
            
            if flagDown :
               
                self.moveBlock2DToStack2D()

                notFullStack = self.getNotFullStack()
                cnt10 = 20 - len(notFullStack)
                if cnt10 > 0 :
                    self.lblCnt.setText(str(int(self.lblCnt.text()) - 1))
                
                if int(self.lblCnt.text()) <= 0:
                    QMessageBox.information(self, '게임종료', '당신이 이겼습니다.')
                    self.flagIng = False
                    return
                for i in range(10):
                    if self.stack2D[4][i] > 0:
                        QMessageBox.information(self,'게임종료','당신이 졌습니다.')
                        self.flagIng = False
                        return
                
                
                
                
                
                
                
                
                
                    
                     
                for i in range(cnt10):
                    notFullStack.insert(0, "0,0,0,0,0,0,0,0,0,0")
                 
                i = 0;
                 
                for str_line in notFullStack:
                    data = str_line.split(",")
                    self.stack2D[i][0] = int(data[0])
                    self.stack2D[i][1] = int(data[1])
                    self.stack2D[i][2] = int(data[2])
                    self.stack2D[i][3] = int(data[3])
                    self.stack2D[i][4] = int(data[4])
                    self.stack2D[i][5] = int(data[5])
                    self.stack2D[i][6] = int(data[6])
                    self.stack2D[i][7] = int(data[7])
                    self.stack2D[i][8] = int(data[8])
                    self.stack2D[i][9] = int(data[9])
                    i+=1
                
                
                
                 
                self.block.myinit()
                
                self.setBlock2DWithBlock()
                
                self.moveStackBlockToScrin() 
        
        self.moveStackBlockToScrin()       
        self.myRender()
        print(self.block)
        
    
    
         

    def keyPressEvent(self, e):
        mykey = e.key()
        self.realPress(mykey)
        
        
    
    def getNotFullStack(self):
        stack_tmp = []
        
        for tmp in self.stack2D :
            if tmp[0] > 0 and tmp[1] > 0 and tmp[2] > 0 and tmp[3] > 0 and tmp[4] > 0 and tmp[5] > 0 and tmp[6] > 0 and tmp[7] > 0 and tmp[8] > 0 and tmp[9] > 0 :
                pass
            else:
                str_line = str(tmp[0])+","+str(tmp[1])+","+str(tmp[2])+","+str(tmp[3])+","+str(tmp[4])+","+ str(tmp[5])+","+str(tmp[6])+","+str(tmp[7])+","+str(tmp[8])+","+str(tmp[9])
                stack_tmp.append(str_line)
        return stack_tmp
        
    def moveBlock2DToStack2D(self):
        for i in range(20):
            for j in range(10):
                if self.block2D[i][j]> 0 :
                    self.stack2D[i][j] = self.block2D[i][j] + 10;
            
        
        
        
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
#                     self.lbl2D[i][j].setStyleSheet("background-color : darkgray; border : 1px solid black")
                    self.lbl2D[i][j].setIcon(QIcon(self.icon))
                if self.scrin2D[i][j] == 1:
#                     self.lbl2D[i][j].setStyleSheet("background-color : red; border : 1px solid black")
                    self.lbl2D[i][j].setIcon(QIcon(self.icon1))
                if self.scrin2D[i][j] == 2:
#                     self.lbl2D[i][j].setStyleSheet("background-color : orange; border : 1px solid black")
                    self.lbl2D[i][j].setIcon(QIcon(self.icon1))
                if self.scrin2D[i][j] == 3:
#                     self.lbl2D[i][j].setStyleSheet("background-color : yellow; border : 1px solid black")
                    self.lbl2D[i][j].setIcon(QIcon(self.icon1))
                if self.scrin2D[i][j] == 4:
#                     self.lbl2D[i][j].setStyleSheet("background-color : green; border : 1px solid black")
                    self.lbl2D[i][j].setIcon(QIcon(self.icon1))
                if self.scrin2D[i][j] == 5:
#                     self.lbl2D[i][j].setStyleSheet("background-color : blue; border : 1px solid black")
                    self.lbl2D[i][j].setIcon(QIcon(self.icon1))
                if self.scrin2D[i][j] == 6:
#                     self.lbl2D[i][j].setStyleSheet("background-color : navy; border : 1px solid black")
                    self.lbl2D[i][j].setIcon(QIcon(self.icon1))
                if self.scrin2D[i][j] == 7:
#                     self.lbl2D[i][j].setStyleSheet("background-color : violet; border : 1px solid black")
                    self.lbl2D[i][j].setIcon(QIcon(self.icon1))
                
                if self.scrin2D[i][j] == 11:
#                     self.lbl2D[i][j].setStyleSheet("background-color : red; border : 1px solid black")
                    self.lbl2D[i][j].setIcon(QIcon(self.icon2))
                if self.scrin2D[i][j] == 12:
#                     self.lbl2D[i][j].setStyleSheet("background-color : orange; border : 1px solid black")
                    self.lbl2D[i][j].setIcon(QIcon(self.icon2))
                if self.scrin2D[i][j] == 13:
#                     self.lbl2D[i][j].setStyleSheet("background-color : yellow; border : 1px solid black")
                    self.lbl2D[i][j].setIcon(QIcon(self.icon2))
                if self.scrin2D[i][j] == 14:
#                     self.lbl2D[i][j].setStyleSheet("background-color : green; border : 1px solid black")
                    self.lbl2D[i][j].setIcon(QIcon(self.icon2))
                if self.scrin2D[i][j] == 15:
#                     self.lbl2D[i][j].setStyleSheet("background-color : blue; border : 1px solid black")
                    self.lbl2D[i][j].setIcon(QIcon(self.icon2))
                if self.scrin2D[i][j] == 16:
#                     self.lbl2D[i][j].setStyleSheet("background-color : navy; border : 1px solid black")
                    self.lbl2D[i][j].setIcon(QIcon(self.icon2))
                if self.scrin2D[i][j] == 17:
#                     self.lbl2D[i][j].setStyleSheet("background-color : violet; border : 1px solid black")
                    self.lbl2D[i][j].setIcon(QIcon(self.icon2))
                
#                 self.lbl2D[i][j].setIconSize(QtCore.QSize(40 , 40))
                
                    
                
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