class Vehicle:
    
    def __init__(self,name,color,kind,value):
        
        self.name = name
        self.color = color
        self.kind = kind
        self.value = value
    
    def description(self):
        desc_str = "{} is a {} {} worth ${:<.2f}.".format(self.name,self.color,self.kind,self.value)
        return desc_str

# Instantiates two objects of class Vehicle
car1 = Vehicle('Ferrari','red','convertible',6000)

car2 = Vehicle('Dodge','blue','truck',10000)


print(car1.description())
print(car2.description())