#include<stdio.h>
#include<stdlib.h>

struct node         //defining the structure of node
{
    int data;
    struct node *next;
};


void printfunction(struct node *n)  // for printing the linked-list
{
    while(n != NULL)
    {
        printf("%d\n ", n->data);
        printf("%d\n ", n->next);
        n = n->next;
    }
}


void push_middle(struct node* prev_node, int middle_data)   // defing the middle push function
{
    struct node* middle_node = (struct node*)malloc(sizeof(struct node)); //allocating the new space for middle insertion data

    
    middle_node->data = middle_data;
    middle_node->next = prev_node->next;
    
    prev_node->next = middle_node;
    
    

}





void push(struct node** head_ref, int new_data)   // def in the begining node insertion
{
    struct node* new_node = (struct node*)malloc(sizeof(struct node));  //allocating the new space in heap
    
    
    
    new_node->data = new_data;
    new_node->next = (*head_ref);
    
    (*head_ref) = new_node;
    
    
    
    
    
    
}


void push_end(struct node* null_node, int end_data)
{
    struct node* last_node = (struct node*)malloc(sizeof(struct node));
    
    last_node->data = end_data;
    last_node->next = null_node->next;
    
    null_node->next = end_data;
    

    
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
    
    push(&head, 59);            // calling the push function
    
    push_middle(second,189);        // calling the push_middle function
    
    push_end(third, 999);
    
    printfunction(head);        // callin the printfunction
    
}
