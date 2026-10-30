#include<stdio.h>
void enqueue(int queue[], int data, int size, int rear,int front)
{
    if (rear == size - 1)
    {
        printf("Overflow\n");        
        return;
    }

    (rear)++;
    queue[rear] = data;
    printf("Data pushed successfully\n");
}

void dequeue(int queue[], int front)
{
    if (front == -1)
    {
        printf("queue is Underflow!\n");
    }
    else
    {
        printf("dequeue data: %d\n", queue[front]);
        (front)--;
    }
}

void display(int queue[], int front)
{
    int i;

    if (front == -1)
    {
        printf("queue is empty\n");
    }
    else
    {
        printf("queue elements are:\n");

        for (i = front; i >= 0; i--)
        {
            printf("%d\n", queue[i]);
        }
    }
}

int main()
{
    int size = 5;
    int queue[5];
    int front = -1, choice, n;
    int rear= -1;

    do
    {
        printf("\n1. enqueue data\n");
        printf("2.  dequeue data\n");
        printf("3. Display stack\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice)
        {
            case 1:
                printf("Enter stack data: ");
                scanf("%d", &n);
                enqueue(queue, n, size, rear);
                break;

            case 2:
                dequeue(queue, &front);
                break;

            case 3:
                display(queue,front);
                break;

            case 4:
                printf("Exiting program\n");
                break;

            default:
                printf("Invalid choice\n");
        }

    } while (choice != 4);

    return 0;
}