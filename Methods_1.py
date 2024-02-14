class Circle():

    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius

    def area(self):
        result = self.radius**2
        result = result *Circle.pi
        return result

    def perimeter(self):
        return self.radius*2*self.pi
    
    def multiply_radius(self,number):
        self.radius = self.radius*number
        print(f'radius is changes to {self.radius}')


mycircle = Circle(radius=4)
print(mycircle.area())
print(mycircle.perimeter())
mycircle.multiply_radius(20)
