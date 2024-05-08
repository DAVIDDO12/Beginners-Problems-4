a = int(input("Enter the number: ")) 
b = int(input("Enter the range: "))
if a<0:
    print("Not a positive integer.Enter a positive integer.")
if b<0:
    print("Not a positive integer.Enter a positive integer.")
for num in range(1, b + 1):
    print(f"{a} x {num} = {a * num}")


