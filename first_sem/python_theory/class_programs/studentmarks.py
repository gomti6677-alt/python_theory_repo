name=""
rollno=0
m1,m2,m3=0,0,0
tot=0.00
avg,per=0.00,0.00
grade=""
avg=tot/300
def percentage():
    global per
    per=avg*100
def grade():
    global grade
    if(per>85):
        grade='distinction'
    elif(per>60):
        grade='first class'
    else:
        pass
def result():
    print("roll no is:",rollno)
    print("name is:",name)
    print("total is:",tot)
    print("average is:",avg)
    print("percentage is:",per)
    print("grade is:",grade)

for i in range(3):
    data()
    total()
    average()
    percentage()
    grade()
    result() 
