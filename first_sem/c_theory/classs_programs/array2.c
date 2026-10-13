#include<stdio.h>

int main(){

    int arraysize=read_array_size();
    int isvalid=validdate_array_size(arraysize);
    if (isvalid ==1)
    {
        int arraysize=read_array_size();
        int isvalided=validate_array_size(arraysize);
        if(validate == 1){

            break;
        }
        printf("please try again");
    }
}
//reads array SIZE from KB
int read_array_size(){   
    int size;  //local variable
    printf("enter the array[>4]:");
    scanf("%d",&size);
    return size;
}


int validsate_array_size(int array_size){
    if(array_size>4){
        return 1;

    }
} 