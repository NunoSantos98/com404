number=int(input("How many zones must I cross?\n"))
print("Crossing zones...")

while(number!=0):
    print("...crossed zone " + str(number))
    number-=1

print("Crossed all zones. Jumanji!")