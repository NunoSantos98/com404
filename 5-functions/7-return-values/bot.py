def sum_weight(beep_weight,bop_weight):
    total_weight=beep_weight+bop_weight

    return total_weight

def calc_avg_weight(beep_weight,bop_weight):
    avg_weight=(beep_weight+bop_weight)/2

    return avg_weight


def run():
    beep_weight=int(input("What is the weight of Beep?"))

    bop_weight=int(input("What is the weight of Bop?"))

    decision=input("What would you like to calcluate (sum or average)?")

    if(decision=="sum"):
        print("The sum of Beep and Bop's weight is "+ str(sum_weight(beep_weight,bop_weight)))

    elif(decision=="average"):
        print("The avg of Beep and Bop's weight is " + str(calc_avg_weight(beep_weight,bop_weight)))

    else:
        print("invalid decision")

run()