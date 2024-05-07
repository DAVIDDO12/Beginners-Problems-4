a = int(input("Enter the number: ")) 
b = int(input("Enter the range: "))
for i in range(1, b + 1):
    print(f"{a} x {i} = {a * i}")
if a<0:
    print("Not a positive integer.Enter a positive integer.")


