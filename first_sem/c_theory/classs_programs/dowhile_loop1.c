#include<stdio.h>
int main()
{
    int choice;
    float a;
    float b;
    float sum;
    float multiplication;
    float division;
    float difference;
    printf("----welcome to my calculater---\n");
    printf("enter a:");
    scanf("%f",&a);
    printf("enter b:");
    scanf("%f",&b);
    printf("1.add\n");
    printf("2.subtract\n");
    printf("3.multiply\n");
    printf("4.divide\n");
    printf("enter your choice:");
    scanf("%d",&choice);
    if(choice==1)
    {
        sum=a+b;
        printf("the sum of %.2f and %.2f is %.2f",a,b,sum);
    }
    else if (choice==2)
    {
        difference=a-b;
        printf("the subtraction of %.2f and %.2f is %.2f",a,b,difference);
    }
    else if (choice==3)
    {
        multiplication=a*b;
        printf("the multiplication od %.2f and %.2f is %.2f",a,b,multiplication);
    }
    else
    {
        division=a/b;
        printf("the division od %.2f and %.2f is %.2f",a,b,division);
    }
    return 0;
}    