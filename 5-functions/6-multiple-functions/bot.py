def display_ladder(step):
    for showing in range (0,step,1):
        print("| |")
        print("***")

def create_ladder():
    step=int(input("How many steps remain?"))
    display_ladder(step)

create_ladder()