
#Animal 클래스의 정의
#default는 public

class Animal:
    def __init__(self):
        self.age = 0
    
    def getOlder(self):
        self.age += 1


class Bird:
    def __init__(self):
        self.mydist = 0
        
    def fly(self):
        self.mydist += 5
        
#Animal 클래스를 상속받는 Human클래스 정의        
class Human(Animal,Bird):
     
    def __init__(self):
        Animal.__init__(self)
        Bird.__init__(self)
        self.name = "이재용"
     
    def changeName(self,name):
        self.name = name
 
# main 함수
if __name__ == '__main__':
    
    newName = "홍길동"
    a = Animal()
    print("a: Animal의 객체\t\t b: Human의 객체")
    print("getOlder 함수 호출 전  a의 age: ",a.age)
    a.getOlder()
    print("getOlder 함수 호출 후 a의 age: ",a.age)
    b = Human()
    print("getOlder 함수 호출 전 b의 age: ",b.age)    
    b.getOlder()
    print("getOlder 함수 호출 후 b의 age: ",b.age)
    print("changeName 함수 호출 전 b의 name:" +b.name)
    b.changeName(newName)
    print("changeName 함수 호출 전 b의 name:" +b.name)
    b.fly()
    print("fly 함수 호출 후 b의 distance:" ,b.mydist) 
 
 
 
 
 
     