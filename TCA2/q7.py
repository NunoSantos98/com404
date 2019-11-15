word=input("Plese, enter a word: ")

nbr_dots=len(word)

print("\n1 Under - display the word with a line under it")
print("2 Over - display the word with a line over it")
print("3 Both - display the word in an underline and overline")
print("4 Grid - display the word in a grid that is n x n in size")

option=int(input())

if(option==1):
    print(word)
    print(nbr_dots*"*")


elif(option==2):
    
    print(nbr_dots*"*")
    print(word)
    

elif(option==3):
    print(nbr_dots*"*")
    print(word)
    print(nbr_dots*"*")

elif(option==4):

    for row in range(3):
        line = nbr_dots * "*"
        space = "   "

        print( (line + space) * 3)



        if(row<3):
            print( (word +" | ") * 3)

        else:
            print( (word) * 3)


