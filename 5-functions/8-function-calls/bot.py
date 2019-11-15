def box(name):
    value=len(name)

    print(" -"*value)
    print("| " + name + " |")
    print(" -"*value)

def lwr(name):
    print(name.lower())

def upr(name):
    print(name.upper())

def mrd(name):
    print(name[::-1])

def repeat(name):
    
    hmt=int(input("How many times do want to repeat: "))

    for count in range(0, hmt,1):
        lwr(name)
        upr(name)

   
       

 

word=input("Please enter a word: ")

    
print("1) Display in a Box – display the word in an ascii art box") 
print("2) Display Lower-case – display the word in lower-case e.g. hello")
print("3) Display Upper-case – display the word in upper-case e.g. HELLO")
print("4) Display Mirrored – display the word with its mirrored word e.g. Hello | olleH ")
print("5) Repeat – ask the user how many times to display the word and then display the word that many times alternating between upper-case and lower-case.")

option = ""
while (option!=0): 

    option=int(input("Choose a option: "))

    if(option==1):
        box(word)
    elif(option==2):
        lwr(word)
    elif(option==3):
        upr(word)
    elif(option==4):
        mrd(word)
    elif(option==5):
        repeat(word)
    else:
        print("invalid option")    



