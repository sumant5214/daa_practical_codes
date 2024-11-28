#include <stdio.h>
#define MAX 5

void main()
{
    int arr[MAX] = {10, 20, 30, 40, 50}, size, key, low, high,
        mid, flag;
    flag = 0;
    low = 0;
    high = 5;
    printf("\nEnter the element to be searched from the array:");
    scanf("%d", &key);
    while (low <= high)
    {
        mid = (low + high) / 2;
        if (arr[mid] == key)
        {
            flag = 1;
            break;
        }
        else if (arr[mid] > key)
        {
            high = mid - 1;
        }
        else
        {
            low = mid + 1;
        }
    }
    if (flag == 1)
        printf("Element %d found in array at position %d", key,

               mid + 1);
    else
        printf("Element %d not found in array", key);
}