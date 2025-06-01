lst = list(map(float,input("Enter list value :").split()))

if not lst :
    print("List is empty")
else :
    lst.sort(reverse=True)
    print(f"list of descending order : {lst}")