'''Create a class named "Dog". It should have a constructor which accepts its name, age and coat color. You must perform the following operations:
'''

class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        #print("dog class initialized!")
        

    def description(self):
        print(self.name, self.age)

    def get_info(self):
        print(self.color)
        
        
class JackRussellTerrier(Dog):

    def __init__(self, name, age, color, bread, features):
        self.bread = bread
        self.features = features
    
    
    #Dog.__init__(self, name, age, color)

    def DOGfeatures_1(self):
        print('dog name :', self.name)
        print("dog age is :", self.age)
        print("dog color is :", self.color)
        print("dog bread is :", self.bread)

    def DOGfeatures_2(self):
        print("dog features is :", self.features)

class Bulldog(Dog):

    def __init__(self, name, age, color, bread, features):
        self.bread = bread
        self.features = features


    def DOGfeatures_1(self):
        print('dog name :', self.name)
        print("dog age is :", self.age)
        print("dog color is :", self.color)
        print("dog bread is :", self.bread)

    def DOGfeatures_2(self):
        print("dog features is :", self.features)


name = input("enter your dog name : ")
age = int(input("enter your dog age : "))
color= input('enter your dogs colour : ')

dogs = Dog(name,age,color)
dogs.description()
dogs.get_info()

dog_features = JackRussellTerrier()
dog_features = Bulldog()




