#include<stdio.h>

void main()
{
    int A[] = {2,3,5,9,12,16,18,23,25,36,45,49,70};
    int n = sizeof(A)/sizeof(int);
    int x = 43;
    int result = binary_search(A, 0, n-1, x);
    
    printf("key is found %d", result);
}


int binary_search(int list[], int l,int  h, int key)
{
    printf("%d %d %d\n", list , l , h);

    while(l <= h){
        
        if (key == list[l] || key == list[h]){
            return key;
        }
        
        int mid = (l+h)/2;
        
        if (key == list[mid]){
            return key;
        }
        
        if (key < list[mid]){
            h = mid-1;
        }
        
        if (key > list[mid]){
            l = mid + 1;
        }
        
        
    }return 0;
    
}
