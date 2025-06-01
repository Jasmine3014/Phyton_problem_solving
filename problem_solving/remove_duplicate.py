lst = list(map(float,input("Enter list value :").split()))

if not lst :
    print("List is empty")
else :
    unique_lst = list(set(lst))
    print(f"List is : {unique_lst}")