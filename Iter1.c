
#include <stdio.h>
#include <stdlib.h>

// Maximum stack size
#define MAX_SIZE 100

 //postorder
struct Node {
    int data;
    struct Node *left, *right;
};


struct Stack {
    int size;
    int top;
    struct Node** array;
};


struct Node* newNode(int data)
{
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->data = data;
    node->left = node->right = NULL;
    return node;
}


struct Stack* createStack(int size)
{
    struct Stack* stack = (struct Stack*)malloc(sizeof(struct Stack));
    stack->size = size;
    stack->top = -1;
    stack->array = (struct Node**)malloc(stack->size * sizeof(struct Node*));
    return stack;
}


int isFull(struct Stack* stack)
{
    return stack->top - 1 == stack->size;
}

int isEmpty(struct Stack* stack)
{
    return stack->top == -1;
}

void push(struct Stack* stack, struct Node* node)
{
    if (isFull(stack))
        return;
    stack->array[++stack->top] = node;
}

struct Node* pop(struct Stack* stack)
{
    if (isEmpty(stack))
        return NULL;
    return stack->array[stack->top--];
}


void postOrderIterative(struct Node* root)
{
    if (root == NULL)
        return;


    struct Stack* s1 = createStack(MAX_SIZE);
    struct Stack* s2 = createStack(MAX_SIZE);


    push(s1, root);
    struct Node* node;


    while (!isEmpty(s1)) {

        node = pop(s1);
        push(s2, node);


        if (node->left)
            push(s1, node->left);
        if (node->right)
            push(s1, node->right);
    }


    while (!isEmpty(s2)) {
        node = pop(s2);
        printf("%d ", node->data);
    }
}


int main()
{

    struct Node* root = NULL;
    root = newNode(1);
    root->left = newNode(2);
    root->right = newNode(3);
    root->left->left = newNode(4);
    root->left->right = newNode(5);
    root->right->left = newNode(6);
    root->right->right = newNode(7);

    postOrderIterative(root);

    return 0;
}
