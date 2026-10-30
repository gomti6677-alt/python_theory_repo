#include<stdio.h>
int main(){
    int number[5];
    for(int i=0;i<=4;i++){
        printf("input %d array element:,i+1");
        scanf("%d",&number[i]);
    }
    printf("enter the new element:");
    scanf("%d",&newdata);
    printf("enter index value");
    scanf("%d",&index);
    //insertion process to insert 'newdata' atindex 'index
    number[4]=number[3];
    number[3]=number[2];
    number[2]=newdata;
    for (int i =0;i<5;i++){
        printf("%d",number[i]);

    }
    
}




