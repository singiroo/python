import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("tetris.ui")[0]

class Block() :
    def __init__(self):
        self.kind =  1;     # 블록모양
        self.status = 1;    # 블록 방향
        self.i = 1;         # 블록 중심축
        self.j = 5;         # 블록 중심축
    def __str__(self):
        return str(self.kind) + ":" + str(self.status) + ":" + str(self.i) + ":" + str(self.j)   
 
#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
        
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.block2D = []
        self.stack2D = []
        self.scrin2D = []
        self.lbl2D = []
        self.block = Block()
                
        self.initBlock2Dstack2Dscrin2D()
        
        self.scrin2D[0][0] = 1
        self.scrin2D[0][1] = 1
        self.scrin2D[1][1] = 1
        self.scrin2D[2][1] = 1
        
        self.print2D(self.scrin2D) # 화면 찍어보기 
        
        
        for i in range(20):
            arr = []
            for j in range(10):
                pb = QPushButton('', self)
                pb.setGeometry(30*j,30*i,29,29)
                pb.setStyleSheet("background-color : #00ff00")
                arr.append(pb)
            self.lbl2D.append(arr)
            
        self.print2D(self.scrin2D)
        print(self.block)



    def keyPressEvent(self, e):
        mykeytext = e.text()
        
        self.flag_col_bound = False;    # 사이드 벽 부딛침 검사
        self.flag_down = False;   
         
#         # 충돌했을때 블록 값을 충돌전의 값을 담기 위한 변수 
#         self.pre_status = self.block.status;    
#         self.pre_i = self.block.i;
#         self.pre_j = self.block.j;
        
        
#         print(e.text())
        if(mykeytext == 'w') :        # 위
            self.changeBlockStatus();
        
        if(mykeytext == 's') :        # 아래
            self.block.i +=1
            self.flag_down = True;
            
        if(mykeytext == 'a') :     #    왼쪽
            self.block.j -=1
        
        if(mykeytext == 'd') :      #   오른쪽
            self.block.j +=1
        
    
        try:
            self.setBlock2DWithBlock()
        except:    
            print("예외가 발생했습니다.")

            
    
        self.moveStackBlock2Scrin()
        
        self.myrender()
        print(self.block)
        
        
        
        if self.flag_down :
            self.moveBlock2Stack()   
        
        
        
        
        
        
#         print(self.isCollision())    # 블록끼리 겹치지 않게 충돌 확인
#         print(1)
#         if self.flag_col_bound :    # 블록끼리 충돌하거나 벽 밖으로 나가는지 확인
#             # 충돌하면 충돌전의 값으로 다시 전환
#             self.block.status = self.pre_status;
#             self.block.i = self.pre_i;
#             self.block.j = self.pre_j;
#              
#             self.setBlock2DWithBlock();    
#             self.moveStackBlock2Scrin();    
#      
#      
#          if(flag_collision || flag_col_bound) {    // 블록끼리 충돌하거나 벽 밖으로 나가는지 확인
#             // 충돌하면 충돌전의 값으로 다시 전환
#             block.status = pre_status;
#             block.i = pre_i;
#             block.j = pre_j;
#             setBlock2DWithBlock();    // 블록이동
#             moveStackBlock2Scrin();    // 화면이동
#             

     
     
     
     
     
     
     
     
    def isCollision(self) :
        for i in range(20):
            for j in range(10):
                if self.stack2D[i][j] > 0 and self.block2D[i][j] > 0:
                    return True    # 충돌시 true 반환 해서 정지시키기
                 
        return False    # 미출동시는 계속 진행
    
    
     
    
#   블록이 바닥에 닿았을때
    def moveBlock2Stack(self) :
        for i in range(20):
            for j in range(10):
                if(self.block2D[i][j] > 0) :    
                    self.stack2D[i][j] = self.block2D[i][j] + 10
                    
        
    
    def changeBlockStatus(self) :
        if(self.block.kind == 1) :
            pass
            
        if self.block.kind == 2 or self.block.kind == 3 or self.block.kind == 4: 
            if self.block.status == 1:
                self.block.status = 2
            elif self.block.status == 2:     
                self.block.status = 1
        
        if self.block.kind == 5 or self.block.kind == 6 or self.block.kind == 7:
            if self.block.status == 1:
                self.block.status = 2
            elif self.block.status == 2 :
                self.block.status = 3
            elif self.block.status == 3 :
                self.block.status = 4
            else :    
                self.block.status = 1
    
    
        
        
        
    def moveStackBlock2Scrin(self):
        for i in range(20):
            for j in range(10):
                self.scrin2D[i][j] = self.stack2D[i][j] + self.block2D[i][j];

        
        
    def setBlock2DWithBlock(self): 
        for i in range(20) :
            for j in range(10) :
                self.block2D[i][j] = 0;
        

#             //    ㅁㅁ
#             //    ㅁㅁ
            if self.block.kind == 1 :    
                self.block2D[self.block.i][self.block.j]=self.block.kind;
                self.block2D[self.block.i][self.block.j+1]=self.block.kind;
                self.block2D[self.block.i+1][self.block.j]=self.block.kind;
                self.block2D[self.block.i+1][self.block.j+1]=self.block.kind;
            
             
#             // ㅁㅁㅁㅁ
            if self.block.kind == 2: 
                if self.block.status == 1:
                    self.block2D[self.block.i-1][self.block.j]=self.block.kind;
                    self.block2D[self.block.i][self.block.j]=self.block.kind;
                    self.block2D[self.block.i+1][self.block.j]=self.block.kind;
                    self.block2D[self.block.i+ 2][self.block.j]=self.block.kind;
                
                if self.block.status == 2: 
                    self.block2D[self.block.i-1][self.block.j+1]=self.block.kind;
                    self.block2D[self.block.i-1][self.block.j]=self.block.kind;
                    self.block2D[self.block.i-1][self.block.j-1]=self.block.kind;
                    self.block2D[self.block.i-1][self.block.j-2]=self.block.kind;
                
            
             
#             // ㅁㅁ
#             //   ㅁㅁ
            if self.block.kind == 3:     
                if self.block.status == 1: 
                    self.block2D[self.block.i][self.block.j]=self.block.kind;
                    self.block2D[self.block.i][self.block.j-1]=self.block.kind;
                    self.block2D[self.block.i+1][self.block.j]=self.block.kind;
                    self.block2D[self.block.i+1][self.block.j+1]=self.block.kind;
                
                if self.block.status == 2: 
                    self.block2D[self.block.i-1][self.block.j]=self.block.kind;
                    self.block2D[self.block.i][self.block.j]=self.block.kind;
                    self.block2D[self.block.i][self.block.j-1]=self.block.kind;
                    self.block2D[self.block.i+1][self.block.j-1]=self.block.kind;
           
             
#             //      ㅁㅁ
#             //    ㅁㅁ
            if self.block.kind == 4:  
                if self.block.status == 1:  
                    self.block2D[self.block.i-1][self.block.j]=self.block.kind;
                    self.block2D[self.block.i][self.block.j]=self.block.kind;
                    self.block2D[self.block.i][self.block.j+1]=self.block.kind;
                    self.block2D[self.block.i+1][self.block.j+1]=self.block.kind;
                
                if self.block.status == 2: 
                    self.block2D[self.block.i][self.block.j-1]=self.block.kind;
                    self.block2D[self.block.i][self.block.j]=self.block.kind;
                    self.block2D[self.block.i-1][self.block.j]=self.block.kind;
                    self.block2D[self.block.i-1][self.block.j+1]=self.block.kind;
                
              
#             //  ㅁ
#             // ㅁㅁㅁ
            if self.block.kind == 5:  
                if self.block.status == 1: 
                    self.block2D[self.block.i][self.block.j-1]=self.block.kind;
                    self.block2D[self.block.i][self.block.j]=self.block.kind;
                    self.block2D[self.block.i][self.block.j+1]=self.block.kind;
                    self.block2D[self.block.i-1][self.block.j]=self.block.kind;
                
                if self.block.status == 2:  
                    self.block2D[self.block.i-1][self.block.j]=self.block.kind;
                    self.block2D[self.block.i][self.block.j]=self.block.kind;
                    self.block2D[self.block.i+1][self.block.j]=self.block.kind;
                    self.block2D[self.block.i][self.block.j+1]=self.block.kind;
                
                if self.block.status == 3: 
                    self.block2D[self.block.i][self.block.j-1]=self.block.kind;
                    self.block2D[self.block.i][self.block.j]=self.block.kind;
                    self.block2D[self.block.i][self.block.j+1]=self.block.kind;
                    self.block2D[self.block.i+1][self.block.j]=self.block.kind;
                
                if self.block.status == 4: 
                    self.block2D[self.block.i-1][self.block.j]=self.block.kind;
                    self.block2D[self.block.i][self.block.j]=self.block.kind;
                    self.block2D[self.block.i+1][self.block.j]=self.block.kind;
                    self.block2D[self.block.i][self.block.j-1]=self.block.kind;
            
             
#             //    ㅁㅁ
#             //      ㅁ
#             //      ㅁ 
            if self.block.kind == 6:
                if self.block.status == 1: 
                    self.block2D[self.block.i-1][self.block.j-1]=self.block.kind;
                    self.block2D[self.block.i-1][self.block.j]=self.block.kind;
                    self.block2D[self.block.i][self.block.j]=self.block.kind;
                    self.block2D[self.block.i+1][self.block.j]=self.block.kind;
                
                if self.block.status == 2: 
                    self.block2D[self.block.i][self.block.j-1]=self.block.kind;
                    self.block2D[self.block.i][self.block.j]=self.block.kind;
                    self.block2D[self.block.i][self.block.j+1]=self.block.kind;
                    self.block2D[self.block.i-1][self.block.j+1]=self.block.kind;
                
                if self.block.status == 3:
                    self.block2D[self.block.i-1][self.block.j]=self.block.kind;
                    self.block2D[self.block.i][self.block.j]=self.block.kind;
                    self.block2D[self.block.i+1][self.block.j]=self.block.kind;
                    self.block2D[self.block.i+1][self.block.j+1]=self.block.kind;
                
                if self.block.status == 4:
                    self.block2D[self.block.i][self.block.j-1]=self.block.kind;
                    self.block2D[self.block.i][self.block.j]=self.block.kind;
                    self.block2D[self.block.i][self.block.j+1]=self.block.kind;
                    self.block2D[self.block.i+1][self.block.j-1]=self.block.kind;
           
             
#             //    ㅁㅁ
#             //    ㅁ
#             //    ㅁ
            if self.block.kind == 7:
                if self.block.status == 1:  
                    self.block2D[self.block.i-1][self.block.j]=self.block.kind;        
                    self.block2D[self.block.i][self.block.j]=self.block.kind;
                    self.block2D[self.block.i+1][self.block.j]=self.block.kind;
                    self.block2D[self.block.i+1][self.block.j-1]=self.block.kind;
                
                if self.block.status == 2:
                    self.block2D[self.block.i][self.block.j]=self.block.kind;
                    self.block2D[self.block.i][self.block.j-1]=self.block.kind;
                    self.block2D[self.block.i-1][self.block.j-1]=self.block.kind;
                    self.block2D[self.block.i][self.block.j+1]=self.block.kind;
                
                if self.block.status == 3:
                    self.block2D[self.block.i][self.block.j]=self.block.kind;
                    self.block2D[self.block.i-1][self.block.j]=self.block.kind;
                    self.block2D[self.block.i-1][self.block.j+1]=self.block.kind;
                    self.block2D[self.block.i+1][self.block.j]=self.block.kind;
                
                if self.block.status == 4:
                    self.block2D[self.block.i][self.block.j]=self.block.kind;
                    self.block2D[self.block.i][self.block.j-1]=self.block.kind;
                    self.block2D[self.block.i][self.block.j+1]=self.block.kind;
                    self.block2D[self.block.i+1][self.block.j+1]=self.block.kind;
 
    

    def initBlock2Dstack2Dscrin2D(self):
        for i in range(20):
            self.block2D.append([0,0,0,0,0, 0,0,0,0,0]) 
            self.stack2D.append([0,0,0,0,0, 0,0,0,0,0]) 
            self.scrin2D.append([0,0,0,0,0, 0,0,0,0,0]) 
            
            
    def print2D(self,arr):
        print('-------------------------------')
        for line in arr:
            print(line)
    
    
    def myrender(self):
        for i in range(20):
            for j in range(10):
                if self.scrin2D[i][j] == 0:
                    self.lbl2D[i][j].setStyleSheet("background-color : #ffffff")
                    
                    
                if self.scrin2D[i][j] == 1:
                    self.lbl2D[i][j].setStyleSheet("background-color : #ff0000")
                if self.scrin2D[i][j] == 2:
                    self.lbl2D[i][j].setStyleSheet("background-color : #ef0000")
                if self.scrin2D[i][j] == 3:
                    self.lbl2D[i][j].setStyleSheet("background-color : #df0000")
                if self.scrin2D[i][j] == 4:
                    self.lbl2D[i][j].setStyleSheet("background-color : #cf0000")
                if self.scrin2D[i][j] == 5:
                    self.lbl2D[i][j].setStyleSheet("background-color : #bf0000")
                if self.scrin2D[i][j] == 6:
                    self.lbl2D[i][j].setStyleSheet("background-color : #af0000")
                if self.scrin2D[i][j] == 7:
                    self.lbl2D[i][j].setStyleSheet("background-color : #9f0000")
                    
                    
                if self.scrin2D[i][j] == 11:
                    self.lbl2D[i][j].setStyleSheet("background-color : #00ff00")
                if self.scrin2D[i][j] == 12:
                    self.lbl2D[i][j].setStyleSheet("background-color : #00ef00")
                if self.scrin2D[i][j] == 13:
                    self.lbl2D[i][j].setStyleSheet("background-color : #00df00")
                if self.scrin2D[i][j] == 14:
                    self.lbl2D[i][j].setStyleSheet("background-color : #00cf00")
                if self.scrin2D[i][j] == 15:
                    self.lbl2D[i][j].setStyleSheet("background-color : #00bf00")
                if self.scrin2D[i][j] == 16:
                    self.lbl2D[i][j].setStyleSheet("background-color : #00af00")
                if self.scrin2D[i][j] == 17:
                    self.lbl2D[i][j].setStyleSheet("background-color : #009f00")   
        
        
    
        
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 
    
    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
    