#include<stdio.h>
int main()
{
    int n; // no of tickets
    int category;
    int regular=0;
    int premium=0;
    int recliner=0;
    int pregular=0;
    int ppremium=0;
    int precliner=0;
    int total;
    printf("enter number of tickets:");
    scanf("%d",&n);
    printf("---categories---\n");
    printf("1.regular - rs.150\n");
    printf("2.premium - rs.250\n");
    printf("3.recliner - rs.400\n");
    for (int i=1;i<=n;i++)
    {
        printf("enter category for ticket %d (1/2/3):",i);
        scanf("%d",&category);
        if (category==1)
        {
            regular++;
            pregular=pregular+150;
        }
        else if (category==2)
        {
            premium++;
            ppremium=ppremium+250;
        }
        else if (category==3)
        {
            recliner++;
            precliner=precliner+400;
        }
        else
        {
            printf("incorrect option");
            break;
        }
    }   
    printf("---FINAL BILL---\n");
    printf("regular tickets:%d\n",regular);
    printf("premium tickets:%d\n",premium);
    printf("recliner tickets:%d\n",recliner);
    total=pregular+ppremium+precliner;
    printf("total(before discount):%d\n",total);
    if (n>=5)
    {
        printf("discount applied: yes\n");
        total=total-(total*10/100);
        printf("final amount:%d\n",total);
    }
    else
    {
        printf("discount applied:no\n");
        printf("final amount:%d\n",total);
    }
}
    
    