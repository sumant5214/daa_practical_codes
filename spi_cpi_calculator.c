#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// #include <conio.h>

void main()
{
    int i, j, num_of_courses;
    float grade_temp_value, sem1_SPI, sem2_SPI, CPI, sem1_obtained, sem2_obtained;
    char grade[2];
    int cred_temp_value, sem1_cred_total, sem2_cred_total;
    // clrscr();
    sem1_cred_total = sem2_cred_total = sem1_obtained = sem2_obtained = 0;
    printf("Enter the number of courses: ");
    scanf("%d", &num_of_courses);
    printf("\nFor Sem 1:");
    for (i = 0; i < num_of_courses; i++)
    {

        printf("\nEnter the grade for course %d: ", i + 1);
        // scanf("%c", &grade);
        scanf("%s", grade);
        if (strcmp(grade, "AA") == 0)
            grade_temp_value = 10.0;
        else if (strcmp(grade, "AB") == 0)
            grade_temp_value = 9.0;
        else if (strcmp(grade, "BB") == 0)
            grade_temp_value = 8.0;
        else if (strcmp(grade, "BC") == 0)
            grade_temp_value = 7.0;
        else if (strcmp(grade, "CC") == 0)
            grade_temp_value = 6.0;
        else if (strcmp(grade, "CD") == 0)
            grade_temp_value = 5.0;
        else if (strcmp(grade, "DD") == 0)
            grade_temp_value = 4.0;
        else if (strcmp(grade, "FF") == 0)
            grade_temp_value = 0.0;
        else
        {
            grade_temp_value = 0.0;
        }
        // scanf("%c", &grade);
        printf("\nEnter the credit for course %d: ", i + 1);
        scanf("%d", &cred_temp_value);
        sem1_cred_total += cred_temp_value;
        sem1_obtained += (cred_temp_value * grade_temp_value);
    }
    printf("\nFor Sem 2:");
    for (i = 0; i < num_of_courses; i++)
    {
        printf("\nEnter the grade for course %d: ", i + 1);
        scanf("%s", grade);
        if (strcmp(grade, "AA") == 0)
            grade_temp_value = 10.0;
        else if (strcmp(grade, "AB") == 0)
            grade_temp_value = 9.0;
        else if (strcmp(grade, "BB") == 0)
            grade_temp_value = 8.0;
        else if (strcmp(grade, "BC") == 0)
            grade_temp_value = 7.0;
        else if (strcmp(grade, "CC") == 0)

            grade_temp_value = 6.0;
        else if (strcmp(grade, "CD") == 0)
            grade_temp_value = 5.0;
        else if (strcmp(grade, "DD") == 0)
            grade_temp_value = 4.0;
        else if (strcmp(grade, "FF") == 0)
            grade_temp_value = 0.0;
        else
        {
            grade_temp_value = 0.0;
        }
        printf("\nEnter the credit for course %d: ", i + 1);
        scanf("%d", &cred_temp_value);
        sem2_cred_total += cred_temp_value;
        sem2_obtained += (cred_temp_value * grade_temp_value);
    }
    sem1_SPI = sem1_obtained / sem1_cred_total;
    sem2_SPI = sem2_obtained / sem2_cred_total;
    CPI = (sem1_SPI + sem2_SPI) / 2;
    printf("\nSPI of Semester 1: %.2f", sem1_SPI);
    printf("\nSPI of Semester 2: %.2f", sem2_SPI);
    printf("\n\nCPI: %.2f", CPI);
    // getch();
    // getch();
}