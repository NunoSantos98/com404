#presentation
print("\n\nHi Stranger, so this is the end of the world and we need people to help us")
print("But first we need to ask you some questions")
print("How old are you?")
age=int(input())

if((age>15) or (age<45)):
    print("Good, and what is your name?")
    name=input()
    print("\n Hi "+name+ ", did you found some clothes or food in your journey?")
    found=input()
    if(found=="yes"):
        print("Perfect! that's gonna help us")
        print("Last Question, did you have experience fighting zombies?")
        exp=input()
        print("For how long? (in months)")
        time=input()
        if((exp=="yes") or (time>12)):
            print("Great! We need people with your experience, come in")
        if((exp=="yes") or (time>6)):
            print("We will need to teach you some techniques, but come in")
        if((exp=="no") or (time<6)):
            print("Oh god! how are you still alive? come in")

    if(found=="no"):
        print("We can't get you in, we have limited resources")

else:
    print("It's not safe, come quickly!")