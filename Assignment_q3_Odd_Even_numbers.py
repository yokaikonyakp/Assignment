#Write a python program to count the number of even and odd numbers from a series of numbers
#sample numbers = (1,2,3,4,5,6,7,8,9)
#expected output--
#No. of even numbers: 4
#No. of odd numbers: 5

numbers = (1,2,3,4,5,6,7,8,9,)

even, odd= 0, 0

for x in numbers: 

    if x % 2 == 0: 

        even += 1

    else: 

        odd+= 1          

print("Even : ", even) 

print("Odd : ", odd)
