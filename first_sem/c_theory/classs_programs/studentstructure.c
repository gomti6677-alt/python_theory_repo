#include<stdio.h>

//global array of structure 'students' with size 5.
//can be accessed in any method. global scope
struct student
{
    int rollno;
    char name[20];
    int marks[3];
    int total;  // to store total marks
    float average; // to store average marks

};
struct student student_list[5];
//method to initialize 5 stduents
void initialize_student(){
    
    for(int i=0;i<5;i++){
        printf("enter %d student data:",i+1);
        printf("enter student roll number:");
        scanf("%d",&student_list[i].rollno);
        printf("enter student name:");
        scanf("%s",student_list[i].name);
        //to collect 3 subject mark
        for (int j=0;j<3;j++){
            printf("enter %d subject mark:");
            scanf("%d",&student_list[i].marks[j]);

        }
    }
}

//to find tota marks of 3 subjects 
int get_total(){
    for (int i=0;i<5;i++){

    student_list[i].total=student_list[i].marks[0]+student_list[i].marks[1]+student_list[i].marks[2];
}
}
int get_average(){
    for(int i=0;i<5;i++)
    student_list[i].average=student_list[i].total/300;

    }


int display_students(){
    for(int i=0;i<5;i++)
    {
    printf(student_list[i].name,"\t",student_list[i].rollno,"\t",student_list[i].marks,"\t",student_list[i].total,"\t",student_list[i].average);
    }
}


int main(){
    //to store second student data
    //array of structure
struct student students[5];
initialize_student();
get_total();
get_average();
printf("rollno\t\tname\t\tmarks\t\t");
display_students();
}

