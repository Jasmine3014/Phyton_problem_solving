lst = list(map(float,input("Enter list value :").split()))

if not lst :
    print("List is empty")
else :
    largest = max(lst)
    print(f"Largest number in list : {largest}")