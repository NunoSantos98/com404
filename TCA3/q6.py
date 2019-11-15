def is_league_united(hero1,hero2):
    if((hero1=="Superman") and (hero2=="Wonder Woman")):
        return True
    elif ((hero1=="Wonder Woman") and (hero2=="Superman")):
        return True
    else:
        return False

def decide_plan(hero1,hero2):
    if(is_league_united(hero1,hero2)==True):
        return "Time to save the world!"
    else:
        return "We must unite the league!"


def run():
    hero1=input("Please enter the name of the first hero: ")

    hero2=input("Enter the name of the second hero: ")

    choose_option=input("league or plan: ")

    if(choose_option=="league"):
        print(is_league_united(hero1,hero2))

    elif(choose_option=="plan"):
        print(decide_plan(hero1,hero2))

    else:
        print("Invalid command. Please try again")


run()