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

#######################################################################

#### 밑 준비
# 오목 게임 만드는 순서
# 필요한 리소스를 세팅
# 리소스를 이용하여 게임판을 생성
# 실제 게임의 로직을 담당할 로직판 생성

#### 바둑돌 놓기 로직
# 좌표 정보를 이용하여 바둑돌 놓기
# 마우스 클릭에 의한 이벤트 생성 (클릭하면 해당 위치의 아이콘이 바둑돌 아이콘으로 바뀜, 로직판의 정보도 갱신)
# 두 바둑돌의 차례 돌리기 ( 흰돌 -> 흑돌 -> 흰돌 -> 흑돌 -> ...)
# 바둑돌 중복 방지(경고 메시지 출력)

#### 승패 판정 로직
# 한 방향의 같은 바둑돌 카운팅 로직 세우기
# 모든 방향으로 카운팅
# 각 방향의 카운팅 정보가 5개 일 경우 승패 판정 로직
# 게임의 종료 로직(더 이상 진행 불가, 알림 메시지 출력)

#########################################################################

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    
    
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        # 게임을 만드는데 필요한 아이콘 파일을 변수에 저장
        self.ie = QIcon("0.png")
        self.iw = QIcon("1.png")
        self.ib = QIcon("2.png")
        # 게임판 사이즈 조정
        self.resize(800,800)
        # 게임의 로직을 담당하는 로직판 생성
        self.int2d = [
                   [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0], 
                   [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0], 
                   [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0], 
                   [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0], 
                   [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0], 
                   
                   [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0], 
                   [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0], 
                   [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0], 
                   [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0], 
                   [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0], 
                   
                   [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0], 
                   [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0], 
                   [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0], 
                   [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0], 
                   [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0], 
                   
                   [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0], 
                   [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0], 
                   [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0], 
                   [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0], 
                   [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0] 
                ]
        self.arr2d = []
        self.flagTurn = True
        self.winner = ""
        
        for j in range(20):
            arr = []
            for i in range(20):
                pb = QPushButton('', self)
                pb.setGeometry(40 * i,40*j,40,40)
                pb.setIconSize(QtCore.QSize(40 , 40))
                pb.setIcon(QIcon(self.ie))
                position = "{},{}".format(j, i)
                pb.setWhatsThis(position)
                pb.clicked.connect(self.myclick)
#                 print("라라라")
                arr.append(pb)
            self.arr2d.append(arr)
#             print("끝.")
        
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
        for i in range(20):
            for j in range(20):
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