lst = list(map(float,input("Enter list value :").split()))

if not lst :
    print("List is empty")
else :
    lst.sort()
    print(f"list of ascending order : {lst}")