class auto(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class prototipo(auto):
    def __init__(self, name, age, power):
        super().__init__(name,age)
        self.power = power


Tesla = prototipo("Tesla Roaster",2,8000)
print(Tesla.name)
print(Tesla.age)
print(Tesla.power)