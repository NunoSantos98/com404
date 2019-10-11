numbers = int(input("How many numbers should I sum up?"))
count = 0
total = 0

while(count<numbers):
    count += 1
    print("Please enter number "+str(count) +" of "+str(numbers)+":")
    enter_number = int(input())
    total = total + enter_number

print("The answer is", str(total))