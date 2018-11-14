#include<stdio.h>

int main()
{
    int a = 5;
    int *p = &a;
    int **q = &p;
    int ***r = &q;
    printf("the value of p is %d\n ", p);
    printf("the address of *p is %d\n ", *p);
    printf("the address of &a is %d\n ", &a);
    printf("the value of a is %d\n " , a);
    printf("the address of q is %d\n ", q);
    printf("the address of r is %d\n ", r);
    printf("the address of **q is %d\n ", **q);
    printf("the address of **r is %d\n ", **r);
    printf("the address of *q is %d\n ", *q);
    printf("the address of *r is %d\n ", *r);
    printf("the address of ***r is %d\n ", ***r);
}
