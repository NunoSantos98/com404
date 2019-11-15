number = int(input("Please enter a number?"))
count = 0
total = 1

while(count < number):
    count += 1
    total = total  *count

print("The factorial is:", str(total))