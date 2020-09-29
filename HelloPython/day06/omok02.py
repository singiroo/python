import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.Qt import QPixmap, QMessageBox
from PyQt5.QtGui import *
from PyQt5 import QtCore
from tkinter import *
import tkinter.messagebox


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("omok02.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    
    
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.ie = QIcon("0.jpg")
        self.iw = QIcon("1.jpg")
        self.ib = QIcon("2.jpg")
        self.resize(750,750)
        self.int2d = [
                   [0,0,0,0,0, 0,0,0,0,0],
                   [0,1,0,0,0, 0,0,0,0,0], 
                   [0,0,2,0,0, 0,0,0,0,0], 
                   [0,0,0,2,0, 0,0,0,0,0], 
                   [0,0,0,0,2, 0,0,0,0,0],
                    
                   [0,0,0,0,0, 2,0,0,0,0], 
                   [0,0,0,0,0, 0,0,0,0,0], 
                   [0,0,0,0,0, 0,0,0,0,0], 
                   [0,0,0,0,0, 0,0,0,0,0], 
                   [0,0,0,0,0, 0,0,0,0,0]         
                ]
        self.arr2d = []
        self.flagTurn = True
        self.winner = ""
        
        for j in range(10):
            arr = []
            for i in range(10):
                pb = QPushButton('', self)
                pb.setGeometry(75 * i,75*j,75,75)
                pb.setIconSize(QtCore.QSize(75 , 75))
                pb.setIcon(QIcon(self.ie))
                position = "{},{}".format(j, i)
                pb.setWhatsThis(position)
                pb.clicked.connect(self.myclick)
                print("라라라")
                arr.append(pb)
            self.arr2d.append(arr)
            print("끝.")
        
        #self.mydraw()

        
    #self가 지칭하는건 QMainWindow
    def myclick(self):
        if self.winner != "":
           QMessageBox.warning(self, '게임 종료', '게임이 종료되었습니다.')
           return
        
        stone = 0
        if self.flagTurn:
            stone = 1
        elif not self.flagTurn:
            stone = 2    
        posit = self.sender().whatsThis()
        j = (int)(posit.split(',')[0])
        i = (int)(posit.split(',')[1])
        
        if(self.int2d[j][i] != 0):
            QMessageBox.warning(self, '메세지 상자', '이미 돌이 놓여져있습니다.\n돌을 놓을 수 없습니다.', QMessageBox.Yes)
            return
        self.int2d[j][i] = stone
        
        self.mydraw()
        
        mycnt_up = self.getUp(j, i, stone)
        mycnt_dw = self.getDw(j, i, stone)
        mycnt_le = self.getLe(j, i, stone)
        mycnt_ri = self.getRi(j, i, stone)
        mycnt_ul = self.getUl(j, i, stone)
        mycnt_ur = self.getUr(j, i, stone)
        mycnt_dl = self.getDl(j, i, stone)
        mycnt_dr = self.getDr(j, i, stone)
        
        horizon = mycnt_le + mycnt_ri + 1
        vertical = mycnt_up + mycnt_dw + 1
        diag_le = mycnt_ul + mycnt_dr + 1
        diag_ri = mycnt_ur + mycnt_dl + 1
        
        
        if horizon == 5 or vertical == 5 or diag_le == 5 or diag_ri == 5:
            self.winner = "백돌" if self.flagTurn == True else "흑돌"
            QMessageBox.information(self, '게임이 끝났습니다', self.winner+"이 이겼습니다")
        
        print("up :", mycnt_up)
        print("down :", mycnt_dw)
        print("left : ",mycnt_le)
        print("right : ",mycnt_ri)
        print("up-left : ",mycnt_ul)
        print("up-right : ",mycnt_ur)
        print("down-left : ", mycnt_dl)
        print("down-right : ",mycnt_dr)
        
        self.flagTurn = not(self.flagTurn) 
    
        
    def myshow2d(self):
        for i in range(10):
            for j in range(10):
                print(self.intList[i][j], end=" ")
            print()
    
            
    def mydraw(self):
       for i in range(len(self.int2d)):
           for j in range(len(self.int2d[i])):
                if(self.int2d[i][j] == 1):
                   self.arr2d[i][j].setIcon(QIcon(self.iw))
                
                elif(self.int2d[i][j] == 2):
                    self.arr2d[i][j].setIcon(QIcon(self.ib))
        
    
   
    
    def getUp(self,j,i,stone):
        cnt = 0
        
        while True:
            j -= 1
            if  j<0 or j >= len(self.int2d):
                break
            if  i<0 or i>=len(self.int2d):
                break
            if self.int2d[j][i] == stone:
                cnt += 1
            else:
                break
        
        return cnt
    
    def getDw(self,j,i,stone):
        cnt = 0
        
        while True:
            j += 1
            if  j<0 or j >= len(self.int2d):
                break
            if  i<0 or i>=len(self.int2d):
                break
            if self.int2d[j][i] == stone:
                cnt += 1
            else:
                break
        
        return cnt
    
    
    def getLe(self,j,i,stone):
        cnt = 0
        
        while True:
            i -= 1
            if  j<0 or j >= len(self.int2d):
                break
            if  i<0 or i>=len(self.int2d):
                break
            if self.int2d[j][i] == stone:
                cnt += 1
            else:
                break
        
        return cnt
    
    
    def getRi(self,j,i,stone):
        cnt = 0
        
        while True:
            i += 1
            if  j<0 or j >= len(self.int2d):
                break
            if  i<0 or i>=len(self.int2d):
                break
            if self.int2d[j][i] == stone:
                cnt += 1
            else:
                break
        
        return cnt
    
    
    def getUl(self,j,i,stone):
        cnt = 0
        
        while True:
            j -= 1
            i -= 1
            if  j<0 or j >= len(self.int2d):
                break
            if  i<0 or i>=len(self.int2d):
                break
            if self.int2d[j][i] == stone:
                cnt += 1
            else:
                break
        
        return cnt
    
    
    def getUr(self,j,i,stone):
        cnt = 0
        
        while True:
            j -= 1
            i += 1
            if  j<0 or j >= len(self.int2d):
                break
            if  i<0 or i>=len(self.int2d):
                break
            if self.int2d[j][i] == stone:
                cnt += 1
            else:
                break
        
        return cnt
    
    
    def getDl(self,j,i,stone):
        cnt = 0
        
        while True:
            j += 1
            i -= 1
            if  j<0 or j >= len(self.int2d):
                break
            if  i<0 or i>=len(self.int2d):
                break
            if self.int2d[j][i] == stone:
                cnt += 1
            else:
                break
        
        return cnt
    
    
    def getDr(self,j,i,stone):
        cnt = 0
        
        while True:
            j += 1
            i += 1
            if  j<0 or j >= len(self.int2d):
                break
            if  i<0 or i>=len(self.int2d):
                break
            if self.int2d[j][i] == stone:
                cnt += 1
            else:
                break
        
        return cnt
      
                
            
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()