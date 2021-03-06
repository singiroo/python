import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("Increase.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    
    cnt = 1;
    
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.btnIncrease.clicked.connect(self.increase)
        self.btnDecrease.clicked.connect(self.decrease)
        self.btnReset.clicked.connect(self.reset)
        
        
    def increase(self):
        self.cnt += 1
        self.lblNum.setText(str(self.cnt))
    
    def decrease(self):
        self.cnt -= 1
        self.lblNum.setText(str(self.cnt))
    
    def reset(self):
        self.cnt = 1
        self.lblNum.setText(str(self.cnt))

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()