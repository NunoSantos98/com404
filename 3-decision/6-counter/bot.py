count_odd=0
count_even=0

print("Please enter the first whole number")
n1=int(input())

print("Please enter the second whole number")
n2=int(input())

print("Please enter the third whole number")
n3=int(input())


if(n1%2==0):
    count_even+=1
else:
    count_odd+=1

if(n2%2==0):
    count_even+=1
else:
    count_odd+=1

if(n3%2==0):
    count_even+=1
else:
    count_odd+=1

print("There were"+str(count_even)+" even and "+str(count_odd)+" odd numbers.")