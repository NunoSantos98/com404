bars=int(input("How many bars should be charged?"))

charged_bars=0

while(charged_bars<bars):

    charged_bars=charged_bars+1

    print("Charging: " + charged_bars*"█ ")

print("The battery is fully charged")

