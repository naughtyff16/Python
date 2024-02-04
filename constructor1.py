class user:
    age=20
    def addAge(self,age):
        age=age+20
        return age
u= user()
print(u.addAge(u.age))