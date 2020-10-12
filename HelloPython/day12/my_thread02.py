import threading
 
def printChar(start, stop):
    for i in range(start, stop):
        print(chr(i), end="")
        if(i%100 == 0):
            print();
    
    
    
def printNumber(start, stop):
    for i in range(start, stop):
        print(i, end=" ")
        if(i%100 == 0):
            print();
 
 
 
 
if __name__ == '__main__':
      
    t1 = threading.Thread(target=printChar, args=(1, 100000))
    t2 = threading.Thread(target=printNumber, args=(1, 100000))
    t1.start()
    t2.start()
 
    print("Main Thread")