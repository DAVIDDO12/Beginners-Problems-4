a = int(input("Enter the number: ")) 
b = int(input("Enter the range: "))
if a<0:
    print("Not a positive integer.Enter a positive integer.")
if b<0:
    print("Not a positive integer.Enter a positive integer.")
for num in range(1, b + 1):
    multiplier=a * num
    print(multiplier)

prime=int(input("Enter a number:"))
if prime % 2 == 0:
    print("This is not a prime number")
else:
    print("This is a prime number")




