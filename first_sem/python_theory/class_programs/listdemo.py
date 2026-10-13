marks=['sachin',50,55,67,76,89]
#declares aan list 'marks' to store marks of 'sachins'
my_mark=[]
# dynamic initialiszation
for number in range(5):
    newmark=int(input("enter the marks:"))
    my_mark.append(newmark)

print("list elements are:")
for i in range(len(my_mark)):
    print(" ")

    for i in range(len(my_mark)):
        sum+=my_mark[i]