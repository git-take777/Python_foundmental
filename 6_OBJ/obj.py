class Person:
    num_legs = 2
    count = 0
#   contructor
    def __init__(self, name, gender, age):
        self.name = name
        self.age = age
        self.gender = gender
        Person.count += 1

    def walk(self):
        print(f"{self.name} is walking")

john = Person("John", 28, 'male')
print(john.count)
taro = Person("Taro", 30, 'male')
print(taro.count)

# ↓クラス変数はどのインスタンスからでもアクセスできる↓
print(john.num_legs)
print(taro.num_legs)

john.walk()

# インスタンスでできること

# 練習問題
# 1. Carクラスを作成してください。属性として、メーカー、モデル、
# class Car:
#     def __init__(self,model_name, mileage, manufacturer):
#         self.model_name = model_name
#         self.mileage = mileage
#         self.manufacturer = manufacturer
#     def gas(self):
#         print(f"{self.model_name} is running")
#     def breakes(self):
#         print(f"{self.model_name} is stopping")

# ModelX = Car("Model X", 20, "Tesla")
# ModelX.gas()
# ModelX.breakes()