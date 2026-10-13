#process a single string student data of n student roll no, name , mobile no, email id , 5 subject marks n get the sub total
# implemented using nested list, use functions and methods n u have to identify the sub tassk
def details():

    name=input("enter ur name:")
    phone=int(input("enter ur phone:"))
    email=input("enter ur email id:")
    rollno=int(input("enter ur rollno:"))
    #append 
    studentdata=[name,phone,rollno,email]
    return studentdata
def listntotal():

    size=int(input("enter the no of subjects:"))
    sum=0
    marks=[]
    for i in range(size):
        mark=int(input("enter marks:"))
        marks.append(mark)
        sum=sum+mark
    return marks,sum

num=int(input("enter number of students"))
studentlist=[ ]
for i in range(num):
    data= details()
    markslist,total=listntotal()
    data.append(markslist)
    data.append(total)
    studentlist.append(data)
print(studentlist)