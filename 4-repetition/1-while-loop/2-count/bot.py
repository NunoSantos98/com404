avoid_cables=int(input("How many live cables must I avoid?"))

live_cables=0

while(live_cables<avoid_cables):
    print("Avoiding...Done!" , end=" ")
    
    live_cables=live_cables+1

    print(str(live_cables) + " live cables avoided")

print("All live cables have been avoided")

