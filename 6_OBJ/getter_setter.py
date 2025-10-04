class Person:
  
    def __init__(self, name, age):
        self.name = name
        # self.age = age
        self._age = age
        # @propertyを使うこともできる→get_ageをageに変更
    @property
    def age(self):
        print("get_age is called")
        return self._age
    @age.setter
    def age(self, age):
        print("set_age is called")
        if age < 0:
            print("Age cannot be negative")
        else:
            self._age = age
    # age = property(get_age, set_age)
john = Person("John", -20)
print(john.name)
print(john.age)
