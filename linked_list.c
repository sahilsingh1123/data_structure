#include<stdio.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node *next;
};


void printfunction(struct node *n)
{
    while(n != NULL)
    {
        printf("%d\n ", n->data);
        printf("%d\n ", n->next);
        n = n->next;
    }
}



int main()
{
    struct node* head = NULL;                          
    struct node* second = NULL;
    struct node* third = NULL;
    
    head = (struct node*)malloc(sizeof(struct node));
    second = (struct node*)malloc(sizeof(struct node));
    third = (struct node*)malloc(sizeof(struct node));
    
    head->data = 76;
    head->next = second;
    
    second->data = 65;
    second->next = third;
    
    third->data = 12;
    third->next = NULL;
    
    printfunction(head);
    
}
