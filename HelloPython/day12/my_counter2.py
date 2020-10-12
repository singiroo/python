import sys
import threading, time
from PyQt5.QtWidgets import *
from PyQt5 import uic


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("button2.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #버튼에 기능을 연결하는 코드
        self.pushButton.clicked.connect(self.start);

    #increase이 눌리면 작동할 함수
    def start(self) :
        t = threading.Thread(target = self.increaseNum);
        t.start();
        
    
    def increaseNum(self):
        for i in range(9):
            time.sleep(1);
            number = int(self.label.text());
            number += 1;
            self.label.setText(str(number));
                


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()



