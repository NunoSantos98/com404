number=input("Write a 5 digit-number:\n")

size_number=len(number)



print("1) Display ASCII Triangle - display the number in an ascii art triangle.")
print("2) Display Left Digits Triangle - display digits of the number so that they form a triangle aligned on the left.")
print("3) Display Right Triangle – display the digits of the number so that they form a triangle aligned to the right.")

option=int(input())

#if(option==1):




if(option==2):

    for row in range(0, size_number):
        for column in range(0, row + 1):
            print(number)
        print("")



#elif(option==3):




