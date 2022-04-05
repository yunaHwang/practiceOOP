
class User:
    count = 0
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password 
        User.count += 1

    def __str__(self):
        #던더 메소드 (더블 언더 메소드)
        return "사용자:{}, 이메일:{}".format(self.name, self.email)

    def say_hello(self):
        print("안녕하세요, 저는 {}입니다".format(self.name))

    def login(self,email,my_password):
        if (self.email == email and self.password == my_password):
            print("로그인 성공")
        else:
            print("로그인 실패")

    def check_name(self,name):
        return self.name == name
    
    @classmethod
    #instance method로도 작성가능하나 통상적 x. (self를 쓰지 않고, User.count와 같이 쓰기 때문)
    #또, instance가 없을 때 class method 사용가능. 
    def number_of_users(cls):
        print(cls.count)




user4 = User('Yeonsoo','yeonsoo@gmail.com','12345')
user5 = User('Yuna','rdking9812@naver.com','45678')



#print(user4)
#print(User.count)
User.number_of_users()
user5.number_of_users()