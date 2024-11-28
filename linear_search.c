#include <stdio.h>
#define MAX 1000
void main()
{
    int arr[MAX], flag, size, key, i;
    flag = 0;
    printf("\nEnter the size of array: ");
    scanf("%d", &size);
    printf("\nEnter the elements of the array: ");
    for (i = 0; i < size; i++)
    {
        scanf("%d", &arr[i]);
    }
    printf("\nEnter the element to find in the array: ");
    scanf("%d", &key);
    for (i = 0; i < size; i++)
    {
        if (arr[i] == key)
        {
            flag = 1;
            break;
        }
    }
    if (flag == 0)
        printf("\nElement %d not found in array", key);

    else
        printf("\nElement %d found in array at position %d",

               key, i + 1);
}