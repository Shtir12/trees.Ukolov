#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *pravoe;
    struct node *levoe;
};

struct node* search(struct node *root, int x)
{
    if(root==NULL || root->data==x)
        return root;
    else if(x>root->data)
        return search(root->pravoe, x);
    else
        return search(root->levoe,x);
}

struct node* find_minimum(struct node *root)
{
    if(root == NULL)
        return NULL;
    else if(root->levoe != NULL)
        return find_minimum(root->levoe);
    return root;
}

struct node* new_node(int x)
{
    struct node *p;
    p = malloc(sizeof(struct node));
    p->data = x;
    p->levoe = NULL;
    p->pravoe = NULL;

    return p;
}

struct node* insert(struct node *root, int x)
{
    if(root==NULL)
        return new_node(x);
    else if(x>root->data)
        root->pravoe = insert(root->pravoe, x);
    else
        root->levoe = insert(root->levoe,x);
    return root;
}

struct node* delete(struct node *root, int x)
{
    if(root==NULL)
        return NULL;
    if (x>root->data)
        root->pravoe = delete(root->pravoe, x);
    else if(x<root->data)
        root->levoe = delete(root->levoe, x);
    else
    {
        if(root->levoe==NULL && root->pravoe==NULL)
        {
            free(root);
            return NULL;
        }
        else if(root->levoe==NULL || root->pravoe==NULL)
        {
            struct node *temp;
            if(root->levoe==NULL)
                temp = root->pravoe;
            else
                temp = root->levoe;
            free(root);
            return temp;
        }
        else
        {
            struct node *temp = find_minimum(root->pravoe);
            root->data = temp->data;
            root->pravoe = delete(root->pravoe, temp->data);
        }
    }
    return root;
}

void inorder(struct node *root)
{
    if(root!=NULL)
    {
        inorder(root->levoe);
        printf(" %d ", root->data);
        inorder(root->pravoe);
    }
}

int main()
{
    /*
                   10
                 /    \
                /      \
               5       20
             /   \     /\
            /     \   /  \
           1      10 15  30
                /          \
               /            \
              9             35
    */
    struct node *root;
    root = new_node(10);
    insert(root,5);
    insert(root,1);
    insert(root,10);
    insert(root,9);
    insert(root,20);
    insert(root,15);
    insert(root,30);
    insert(root, 35);
\

    inorder(root);
    printf("\n");

    root = delete(root, 1);
    /*
                   10
                 /    \
                /      \
               5       20
                 \     /\
                  \   /  \
                 10 15  30
                /          \
               /            \
              9             35
    */

    root = delete(root, 30);
    /*
                   10
                 /    \
                /      \
               5       20
                 \     /\
                  \   /  \
                  10 15  35
                /
               /
              9
    */


    root = delete(root, 35);
    /*
                   10
                 /    \
                /      \
               5       20
                 \     /
                  \   /
                  10 15
                /
               /
              9
    */
    root = delete(root, 9);
    inorder(root);
    /*
                   10
                 /    \
                /      \
               5       20
                 \     /
                  \   /
                  10 15                      
    */
    printf("\n");

    return 0;
}
