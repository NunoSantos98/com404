print("Please enter a whole number")
number= int(input())

if(number%2== 0):
    print(str(number) + " it's a even number")
elif(number%2== 1):
    print(str(number) + " it's a odd number")
else:
    print("error...returning nothing")

