class Player():

    def __init__(self,name, age, superpower):
        print("started constructing player")
        self.name=name
        self.age=age
        self.superpower=superpower


    def get_name(self):
        return self.name[0].lower[]+self.name[1:]
player1=Player("John",20,"super strength")
player2=Player("Ramesh",20,"flying")




# print(player1)  
# print(type(player1))
# print(player1.name)#direct accessing method
# print(player1.age)
# print(player1.superpower)
