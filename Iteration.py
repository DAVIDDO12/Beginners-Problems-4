a = int(input("Enter the number: ")) 
b = int(input("Enter the range: "))
if a<0:
    print("Not a positive integer.Enter a positive integer.")
else:
    for num in range(1, b + 1):
     multiplier=a * num
     print(multiplier)
if b<0:
    print("Not a positive integer.Enter a positive integer.")

count = 0
number=int(input("Enter a number:"))
if number == 1:
    print("This is not a prime.")
elif number > 1:
    for prime in range(2,number):
        if (number % prime) == 0:
         count += 1
         break
if count == 1:
    print("This is not a prime.")
else:
    print("This is a prime.")

number=int(input("Enter a number:"))
if number % 3 == 0:
    print("Fizz")
if number % 5 == 0:
    print("Buzz")
if number % 15 == 0:
    print("Fizzbuzz")


