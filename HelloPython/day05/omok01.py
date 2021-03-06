import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.Qt import QPixmap
from PyQt5.QtGui import *
from PyQt5 import QtCore


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("omok01.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    
    msg = True
    range (0, 10)
    imageList=[[0]*10]*10
    intList=[[0]*10]*10
    
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.ie = QIcon("0.jpg")
        self.iw = QIcon("1.jpg")
        self.ib = QIcon("2.jpg")
        self.resize(800,800)
        self.int2d = [
                   [0,0,0,0,0, 0,0,0,0,0],
                   [0,1,0,0,0, 0,0,0,0,0], 
                   [0,0,2,0,0, 0,0,0,0,0], 
                   [0,0,0,2,0, 0,0,0,0,0], 
                   [0,0,0,0,2, 0,0,0,0,0],
                    
                   [0,0,0,0,0, 0,0,0,0,0], 
                   [0,0,0,0,0, 0,0,0,0,0], 
                   [0,0,0,0,0, 0,0,0,0,0], 
                   [0,0,0,0,0, 0,0,0,0,0], 
                   [0,0,0,0,0, 0,0,0,0,0]         
                ]
        self.arr2d = []
        
        
        
        for j in range(10):
            arr = []
            for i in range(10):
                pb = QPushButton('', self)
                pb.setGeometry(75 * i,75*j,75,75)
                pb.setIconSize(QtCore.QSize(75 , 75))
                pb.setIcon(QIcon(self.ie))
                position = "{},{}".format(j, i)
                pb.setWhatsThis(position)
                #pb.clicked.connect(self.mydraw)
                arr.append(pb)
            self.arr2d.append(arr)
        
        self.mydraw()
        
    #self가 지칭하는건 QMainWindow
    def myclick(self):
        posit = self.sender().whatsThis()
        j = (int)(posit.split(',')[0])
        i = (int)(posit.split(',')[1])
        self.intList[j][i] = 1
        print(self.intList[j][i])
        self.sender().setIcon(QIcon(self.iw))
        
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
        
      
                
            
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()