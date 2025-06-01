lst = list(map(float, input("Enter numbers separated by spaces: ").split()))

if len(lst) < 2:
    print("List must have at least 2 elements")
else:
    lst.sort()
    print(f"Sorted list in ascending order: {lst}")
    print(f"The second largest element is: {lst[-2]}")

    sorted_lst = sorted(lst, reverse=True)
    print(f"The second largest element is: {sorted_lst[1]}")