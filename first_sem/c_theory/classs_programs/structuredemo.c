#include<stdio.h>
struct student{
    int id;
    char name[10]; //for name
    char contact[10]; //for contact no
    int pin; //for pin code
};
int main(){    //creating structure variablr 'firststudent, of type 'student'
    struct student firststudent;
    struct student secondstudent;
    firststudent.id=100; //member 'id' of 'firststudent' initialized with 100
    secondstudent.id=101;
    firststudent.name=("gomti");
    secondstudent.name=("falak");
    firststudent.contact=("1234567897");
    secondstudent.contact=("3236474849");
    firststudent.pin="123912";
    secondstudent.pin="232322";
}