class Person():

    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def hello(self):
        print("Hello!")

    def report(self):
        print(f"I and {self.first_name} {self.last_name}")

class Agent(Person):

    def __init__(self,first_name,last_name,code_name):
        Person.__init__(self,first_name,last_name)
        self.code_name = code_name

    #Overwrite report method specific to Agent()
    def report(self):
        print("I'm here!")

    def reveal(self,passcode):

        if passcode == 123:
            print("I and a secret agent")
        else:
            self.report()

x = Agent("John","Smith","Mr. X")
print(x.code_name)
x.reveal(123)