print("What is your name human?")
name=input()

print("How old are you (in years)?")
age=int(input())

print("How tall are you (in meters)?")
height=float(input())

print("How much do you weigh (in kilograms)?")
weigh=int(input())

bmi=weigh/(height*height)

print(name+" you are "+str(age)+" years old and your bmi is "+str(bmi)+"")