lst = list(map(float,input("Enter list value :").split()))

if not lst :
    print("List is empty")
else :
    product = 1
    for num in lst :
        product *= num
    print(f"Multipication of the sum is : {product}")

