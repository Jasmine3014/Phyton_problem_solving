lst = list(map(float,input("Enter list value :").split()))

if not lst :
    print("List is empty")
else :
    miniumum = min(lst)
    print(f"Largest number in list : {miniumum}")