lst = list(map(float,input("Enter list value :").split()))

if not lst :
    print("List is empty")
else :
    sum_lst = sum(lst)
    print(f"sum of the list is : {sum_lst}")