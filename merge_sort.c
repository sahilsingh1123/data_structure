#include<stdio.h>
#include<stdlib.h>


int main()
{
    int A[] = {2,5,6,7};
    int B[] = {3,4,8,9};
    
    int size_A = sizeof(A)/sizeof(int);
    int size_B = sizeof(B)/sizeof(int);
    
    merge(A,B,size_A, size_B);
    

}



void print_function(int C[], int size_c)
{
    int k;
    for (k=0;k<size_c;k++)
        {
            printf("the new merged array is %d \n", C[k]);
        }
}


int merge(int A[], int B[],int m, int n)
{
    int i=0, j=0;
    int k = m+n;
    int C[k];
    
    while(i<=m && j<=n)
    {
       
    
    
        if (A[i]<B[j])
        {
            C[k] = A[i];
            
            i++;
        }
        else
        {
            C[k] = B[j];
           
            j++;
        }
        k++;
        
         int size_c = (m+n);
    print_function(C, size_c);
        
    } 
   
   
}
