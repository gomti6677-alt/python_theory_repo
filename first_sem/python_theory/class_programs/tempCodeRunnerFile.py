
def data():
    global name,rollno,m1,m2,m3
    name=input("enter name:")
    rollno=int(input("enter rollno:"))
    m1=int(input("enter marks 1:"))
    m2=int(input("enter marks 2:"))
    m3=int(input("enter marks 3:"))
def total():
    global tot
    tot=m1+m2+m3
def average():
    global avg