#include<stdio.h>

int sum_of_all_array(int A[],int size)
{
    int i; int sum = 0;
    for(i=0;i<size;i++)
    {
        sum = sum + A[i];
    }
   return sum; 
}

int main()
{
    int A[] = {1,2,3,4,5};
    int size = sizeof(A)/sizeof(A[0]);
    
    int total = sum_of_all_array(A,size);
    
    printf("sum of the aray is...%d \n", total);
    
}
