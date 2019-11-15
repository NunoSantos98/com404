life=100

print("Your health is " + str(life) + "%. Escape is in progress...\n")


for nmb_count in range(0,5):
    
    question=input("…Oh dear, who is that?\n")
    
    
    if(question=="Smiler's Bot"):
        print("Time to jam out of here!\n")
        life=life-20

    elif(question=="Hacker"):
        print("Yay! Better follow this one!\n")
        life=life+20

    else:
        print("Phew, just another emoji!\n")

print("Escaped! Health is "+str(life)+"%")