def gcd(a,b):
    while b:
        a,b = b, a%b
    return a

num1 = int(input("Enter value of a:"))
num2 = int(input("Enter value of b:"))

result = gcd(num1,num2)
print(f"GCD IS : {result}")