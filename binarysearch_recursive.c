#include<stdio.h>

void main()
{
    int A[] = {2,3,5,9,12,16,18,23,25,36,45,49,70};
    int n = sizeof(A)/sizeof(int);
    int x = 3;
    int result = binary_search(A, 0, n-1, x);
    if (result == -1){
           printf("key is  not found %d");
    }
    else printf("key is found %d\n", result);
}


int binary_search(int list[], int l,int  h, int key)
{
    printf("%d %d %d\n", list , l , h);
    
    
    if (list[l]<=list[h]){
        if (key == list[l] || key == list[h]){
            return key;
        }
        int mid = (l+h)/2;
        if (key == list[mid]){
            return key;
        }
        
        if (key<list[mid]){
            return binary_search(list, l, mid-1, key);
        }
        if (key>list[mid]){
            return binary_search(list, mid+1, h, key);
        }
        
        
        
    } 
    
    return -1; 
}
