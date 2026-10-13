//write a program ot create an array to store and display5 subjects marks
#include<stdio.h>
int main()
{
    int subject_marks[5];   //declare an array 'sub_marks'
    // with SIZE 5 of 'int' type
    //storing data/ array initialization - array_name[index]=data/value;
    subject_marks[0]=80; //store the value '80' in  an array position whose index is '0'
    subject_marks[1]=78;
    subject_marks[2]=68;
    subject_marks[3]=58;
    subject_marks[4]=88;   //starting array intialization
    //fetch first array elemenmt from 'subject_marks'
    printf("first subject marks:%d",sub_marks[0]);
    printf("second subject marks:%d",sub_marks[1]);
    printf("third subject marks:%d",sub_marks[2]);
    printf("fourth subject marks:%d",sub_marks[3]);
    printf("fifth subject marks:%d",sub_marks[4]);

    


}