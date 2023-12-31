series = []
A = int(input("How many numbers you want to add in list"))
for i in range(A):
    elements = int(input(f"Enter element {i+1}"))
    series.append(elements)
print(series)
odd_num = []
even_num = []
for i in series:
    if i%2==0:
        even_num.append(i)
    else:
        odd_num.append(i)
print("Number of even numbers :",len(even_num))
print("Number of odd numbers :",len(odd_num))
