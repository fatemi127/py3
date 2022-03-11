mt_lst = []
n = int (input("Please Enter The Numbers of Elements:\n"))

for i in range (0,n):
    elements = int (input("Enter the numbers:\n"))
    mt_lst.append(elements)
mt_lst.sort()
print(mt_lst)