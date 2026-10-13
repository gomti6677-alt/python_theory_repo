#include <stdio.h>
#include<string.h>

#define STUDENTS 5
#define SUBJECTS 5

struct Student {
    int rollNo;
    char name[50];
    int marks[SUBJECTS];
    int total;
    float average, percentage;
    char result[10];
};

void inputStudents(struct Student s[]) {
    int i, j;

    for (i = 0; i < STUDENTS; i++) {
        printf("\nEnter details of Student %d\n", i + 1);

        printf("Enter Roll Number: ");
        scanf("%d", &s[i].rollNo);

        printf("Enter Name: ");
        scanf(" %49[^\n]", s[i].name);

        for (j = 0; j < SUBJECTS; j++) {
            do {
                printf("Enter marks in Subject %d (0-100): ", j + 1);
                scanf("%d", &s[i].marks[j]);

                if (s[i].marks[j] < 0 || s[i].marks[j] > 100) {
                    printf("Invalid marks! Enter marks between 0 and 100.\n");
                }
            } while (s[i].marks[j] < 0 || s[i].marks[j] > 100);
        }
    }
}

void calculateResults(struct Student s[]) {
    int i, j, pass;

    for (i = 0; i < STUDENTS; i++) {
        s[i].total = 0;
        pass = 1;

        for (j = 0; j < SUBJECTS; j++) {
            s[i].total += s[i].marks[j];

            if (s[i].marks[j] < 35) {
                pass = 0;
            }
        }

        s[i].average = s[i].total / 5.0;
        s[i].percentage = (s[i].total / 500.0) * 100;

        if (pass == 1) {
            strcpy(s[i].result, "PASS");
        } else {
            strcpy(s[i].result, "FAIL");
        }
    }
}

void displayResults(struct Student s[]) {
    int i;

    printf("\n================ STUDENT RESULT SHEET ================\n");

    printf("%-6s %-15s %4s %4s %4s %4s %4s %6s %7s %9s %6s\n",
           "RollNo", "Name", "S1", "S2", "S3", "S4", "S5",
           "Total", "Average", "Percent", "Result");

    printf("--------------------------------------------------------------------------\n");

    for (i = 0; i < STUDENTS; i++) {
        printf("%-6d %-15s %4d %4d %4d %4d %4d %6d %7.2f %8.2f%% %6s\n",
               s[i].rollNo,
               s[i].name,
               s[i].marks[0],
               s[i].marks[1],
               s[i].marks[2],
               s[i].marks[3],
               s[i].marks[4],
               s[i].total,
               s[i].average,
               s[i].percentage,
               s[i].result);
    }

    printf("==========================================================================\n");
}

int main() {
    struct Student students[STUDENTS];

    inputStudents(students);
    calculateResults(students);
    displayResults(students);

    return 0;
}