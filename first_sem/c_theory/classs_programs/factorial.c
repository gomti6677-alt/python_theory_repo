#include<stdio.h>
int factorial(int number){
    /* base case */
    if (number==0)
    return 1;
    return number * factorial(number-1)
}
   int main ()