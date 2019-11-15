print("Welcome to the planet of Apes...")
human=0
ape=0

for count in range(0,7):
    type=input("…be ye human or be ye ape?\n")

    if(type=="human"):
        human+=1
        print("I did not start this war. But I will finish it.\n")

    if(type=="ape"):
        ape+=1
        print("Apes together strong!\n")

print("Total Humans count: "+ str(human))
print("Total Apes count: "+ str(ape))

    