class Bot:
    def __init__(self,name,age=0,energy=0,shield=0):
        self.name=name
        self.age=age
        self.energy=energy
        self.shield=shield


    def display_name(self):
        print("{} is the name".format(self.name))
  
    def display_age(self):
        print("{} is the age".format(self.age))

    def display_energy(self):
        print("{} is the energy percentage".format(self.energy))

    def display_shield(self):
        print("{} is the shield percentage".format(self.shield))

    def display_summary(self):
        print("name: {}\nAge: {}\nEnergy:{}\nShield:{}".format(self.name,self.age,self.energy,self.shield))

bot=Bot("Nuno",21,60,57)

bot.display_summary()