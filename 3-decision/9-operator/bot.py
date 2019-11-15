print("What type of adventure should I have?")
decision=input()

if(decision=="scary" or decision=="short"):
    print("Entering the dark forest!")
elif(decision=="safe" or decision=="long"):
    print("Taking the safe route!")

else:
    print("Not sure which route to take")