import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("tetris.ui")[0]

class Block():
    def __init__(self) :
        self.kind = 5
        self.status = 1
        self.i = 1
        self.j = 5 
    def myinit(self) :
        self.kind = 5
        self.status = 1
        self.i = 1
        self.j = 5    
             
    def __str__(self):
        return str(self.kind) + ":" +str(self.status) + ":" +str(self.i) + ":" +str(self.j) 

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.block2D = []
        self.stack2D = []
        self.scrin2D = []
        self.lbl2D = []
        self.block = Block()
    
        self.initBlock2DStack2DScrin2D()
        
        self.stack2D[19][0]=11 
        self.stack2D[19][1]=11 
        self.stack2D[19][2]=11 
        self.stack2D[19][3]=11 

        
        for i in range(20):
            arr = []
            for j in range(10):
                pb = QPushButton('', self)
                pb.setGeometry(30*j,30*i,29,29)
                pb.setStyleSheet("background-color: #00ff00")
                arr.append(pb)
            self.lbl2D.append(arr) 
            
        self.myrender()    
        self.print2D(self.scrin2D)
        print(self.block)
        
    def keyPressEvent(self, e):
        # a 좌 s 아래 d 우 w 위
        flag_col_bound = False
        flag_down = False
        pre_status = self.block.status;
        pre_i = self.block.i;
        pre_j = self.block.j;         
        
        mykeytext = e.text()
        if mykeytext == 'a':
            self.block.j -= 1
        if mykeytext == 'd':
            self.block.j += 1  
        if mykeytext == 's':
            self.block.i += 1 
            flag_down = True 
        if mykeytext == 'w':
            self.changeBlockStatus()   
        
        try:
            self.block.j = self.block.j - 10
            self.setBlock2DWithBlock()
            self.block.j = self.block.j + 10
            self.setBlock2DWithBlock()
        except:    
            print('예외가 발생했습니다.')
            flag_col_bound = True
            
        flag_collision = self.isCollision()  
        print("flag_collision",flag_collision)
        
        if flag_collision or flag_col_bound :
            self.block.status = pre_status;
            self.block.i = pre_i;
            self.block.j = pre_j;
            self.setBlock2DWithBlock();
            self.moveStackBlock2Scrin();
            if flag_down : 
                self.moveBlock2Stack()
                notfullStack = self.getNotFullStack()
                cnt10 = 20 - len(notfullStack)
                for i in range(cnt10):
                    notfullStack.insert(0, "0,0,0,0,0,0,0,0,0,0") 
                
                i=0     
                for str_line in notfullStack:
                    data = str_line.split(",")
                    self.stack2D[i][0]= int(data[0])
                    self.stack2D[i][1]= int(data[1])
                    self.stack2D[i][2]= int(data[2])
                    self.stack2D[i][3]= int(data[3])
                    self.stack2D[i][4]= int(data[4])
                    self.stack2D[i][5]= int(data[5])
                    self.stack2D[i][6]= int(data[6])
                    self.stack2D[i][7]= int(data[7])
                    self.stack2D[i][8]= int(data[8])
                    self.stack2D[i][9]= int(data[9])
                    i+=1
                
                
                self.block.myinit()
                self.setBlock2DWithBlock()
                self.moveStackBlock2Scrin()

        self.moveStackBlock2Scrin()
        self.myrender()
        print(self.block)
    def getNotFullStack(self):
        stack_temp = []
        for temp in self.stack2D :
            if  temp[0] > 0 and temp[1] > 0 and temp[2] > 0 and temp[3] > 0 and temp[4] > 0 and temp[5] > 0 and temp[6] > 0 and temp[7] > 0 and temp[8] > 0 and temp[9] > 0 :
                pass
            else :
                str_line = str(temp[0])+","+str(temp[1])+","+str(temp[2])+","+str(temp[3])+","+str(temp[4])+","+ str(temp[5])+","+str(temp[6])+","+str(temp[7])+","+str(temp[8])+","+str(temp[9]);
                stack_temp.append(str_line)
        return stack_temp
        
        
    def moveBlock2Stack(self):
        for i in range(20):
            for j in range(10):
                if self.block2D[i][j]>0 :
                    self.stack2D[i][j] = self.block2D[i][j]+10;

    def isCollision(self):
        for i in range(20):
            for j in range(10):
                if self.stack2D[i][j]>0 and self.block2D[i][j]>0 :
                    return True
        return False;

    def changeBlockStatus(self):
        if self.block.kind == 2 or self.block.kind == 3 or self.block.kind == 4 :
            if self.block.status == 1 :
                self.block.status = 2
            elif self.block.status == 2:
                self.block.status = 1

        if self.block.kind == 5 or self.block.kind == 6 or self.block.kind == 7 :
            if self.block.status == 1 :
                self.block.status = 2
            elif self.block.status == 2 :
                self.block.status = 3
            elif self.block.status == 3 :
                self.block.status = 4
            elif self.block.status == 4:
                self.block.status = 1

        
    def moveStackBlock2Scrin(self): 
        for i in range(20):
            for j in range(10):
                self.scrin2D[i][j] = self.stack2D[i][j]+self.block2D[i][j]

        
    def setBlock2DWithBlock(self):
        for i in range(20):
            for j in range(10):
                self.block2D[i][j] = 0

        if self.block.kind == 1:
            self.block2D[self.block.i]  [self.block.j]      =self.block.kind
            self.block2D[self.block.i]  [self.block.j+1]    =self.block.kind
            self.block2D[self.block.i+1][self.block.j]      =self.block.kind
            self.block2D[self.block.i+1][self.block.j+1]    =self.block.kind
            
            
            
        if self.block.kind == 2 :
            if self.block.status == 1 :
                self.block2D[self.block.i-2][self.block.j]=self.block.kind
                self.block2D[self.block.i-1][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i+1][self.block.j]=self.block.kind
            if self.block.status == 2:
                self.block2D[self.block.i-1][self.block.j+1]=self.block.kind
                self.block2D[self.block.i-1][self.block.j]=self.block.kind
                self.block2D[self.block.i-1][self.block.j-1]=self.block.kind
                self.block2D[self.block.i-1][self.block.j-2]=self.block.kind
        
        if self.block.kind == 3 :
            if self.block.status == 1:
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j-1]=self.block.kind
                self.block2D[self.block.i+1][self.block.j]=self.block.kind
                self.block2D[self.block.i+1][self.block.j+1]=self.block.kind
            if self.block.status == 2 :
                self.block2D[self.block.i-1][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j-1]=self.block.kind
                self.block2D[self.block.i+1][self.block.j-1]=self.block.kind

        if self.block.kind == 4 :
            if self.block.status == 1 :
                self.block2D[self.block.i-1][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j+1]=self.block.kind
                self.block2D[self.block.i+1][self.block.j+1]=self.block.kind

            if self.block.status == 2 :
                self.block2D[self.block.i][self.block.j-1]=self.block.kind
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i-1][self.block.j]=self.block.kind
                self.block2D[self.block.i-1][self.block.j+1]=self.block.kind

        
        if self.block.kind == 5 :
            if self.block.status == 1 :
                self.block2D[self.block.i][self.block.j-1]=self.block.kind
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j+1]=self.block.kind
                self.block2D[self.block.i-1][self.block.j]=self.block.kind

            if self.block.status == 2 :
                self.block2D[self.block.i-1][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i+1][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j+1]=self.block.kind

            if self.block.status == 3 :
                self.block2D[self.block.i][self.block.j-1]=self.block.kind
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j+1]=self.block.kind
                self.block2D[self.block.i+1][self.block.j]=self.block.kind

            if self.block.status == 4 :
                self.block2D[self.block.i-1][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i+1][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j-1]=self.block.kind

        
        if self.block.kind == 6 :
            if self.block.status == 1 :
                self.block2D[self.block.i-1][self.block.j-1]=self.block.kind
                self.block2D[self.block.i-1][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i+1][self.block.j]=self.block.kind

            if self.block.status == 2 :
                self.block2D[self.block.i][self.block.j-1]=self.block.kind
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j+1]=self.block.kind
                self.block2D[self.block.i-1][self.block.j+1]=self.block.kind

            if self.block.status == 3 :
                self.block2D[self.block.i-1][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i+1][self.block.j]=self.block.kind
                self.block2D[self.block.i+1][self.block.j+1]=self.block.kind

            if self.block.status == 4 :
                self.block2D[self.block.i][self.block.j-1]=self.block.kind
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j+1]=self.block.kind
                self.block2D[self.block.i+1][self.block.j-1]=self.block.kind

        if self.block.kind == 7 :
            if self.block.status == 1 :
                self.block2D[self.block.i-1][self.block.j]=self.block.kind        
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i+1][self.block.j]=self.block.kind
                self.block2D[self.block.i+1][self.block.j-1]=self.block.kind

            if self.block.status == 2 :
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j-1]=self.block.kind
                self.block2D[self.block.i-1][self.block.j-1]=self.block.kind
                self.block2D[self.block.i][self.block.j+1]=self.block.kind

            if self.block.status == 3 :
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i-1][self.block.j]=self.block.kind
                self.block2D[self.block.i-1][self.block.j+1]=self.block.kind
                self.block2D[self.block.i+1][self.block.j]=self.block.kind

            if self.block.status == 4 :
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j-1]=self.block.kind
                self.block2D[self.block.i][self.block.j+1]=self.block.kind
                self.block2D[self.block.i+1][self.block.j+1]=self.block.kind


    
    def initBlock2DStack2DScrin2D(self):
        for i in range(20):
            self.block2D.append([0,0,0,0,0, 0,0,0,0,0])
            self.stack2D.append([0,0,0,0,0, 0,0,0,0,0])
            self.scrin2D.append([0,0,0,0,0, 0,0,0,0,0])
        
    def print2D(self,arr):
        print("----------------------------------------------")
        for line in arr:
            print(line)
            
    def myrender(self):
        for i in range(20):
            for j in range(10):  
                if self.scrin2D[i][j] == 0:
                    self.lbl2D[i][j].setStyleSheet("background-color: #ffffff")
                    
                if self.scrin2D[i][j] == 1:
                    self.lbl2D[i][j].setStyleSheet("background-color: #ff0000")   
                if self.scrin2D[i][j] == 2:
                    self.lbl2D[i][j].setStyleSheet("background-color: #ef0000")
                if self.scrin2D[i][j] == 3:
                    self.lbl2D[i][j].setStyleSheet("background-color: #df0000")   
                if self.scrin2D[i][j] == 4:
                    self.lbl2D[i][j].setStyleSheet("background-color: #cf0000")   
                if self.scrin2D[i][j] == 5:
                    self.lbl2D[i][j].setStyleSheet("background-color: #bf0000")
                if self.scrin2D[i][j] == 6:
                    self.lbl2D[i][j].setStyleSheet("background-color: #af0000")                     
                if self.scrin2D[i][j] == 7:
                    self.lbl2D[i][j].setStyleSheet("background-color: #9f0000")
                    
                if self.scrin2D[i][j] == 11:
                    self.lbl2D[i][j].setStyleSheet("background-color: #00ff00")   
                if self.scrin2D[i][j] == 12:
                    self.lbl2D[i][j].setStyleSheet("background-color: #00ef00")
                if self.scrin2D[i][j] == 13:
                    self.lbl2D[i][j].setStyleSheet("background-color: #00df00")   
                if self.scrin2D[i][j] == 14:
                    self.lbl2D[i][j].setStyleSheet("background-color: #00cf00")   
                if self.scrin2D[i][j] == 15:
                    self.lbl2D[i][j].setStyleSheet("background-color: #00bf00")
                if self.scrin2D[i][j] == 16:
                    self.lbl2D[i][j].setStyleSheet("background-color: #00af00")                     
                if self.scrin2D[i][j] == 17:
                    self.lbl2D[i][j].setStyleSheet("background-color: #009f00")
                    
                    
                     

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()