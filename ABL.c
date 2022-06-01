#include <stdio.h>
#include <stdlib.h>

struct Node
{
	int kluch;
	struct Node * levoe;
	struct Node * pravoe;
	int visota;
};

int max(int a, int b);
int height(struct Node *N)
{
	if (N == NULL)
		return 0;
	return N->visota;
}

int max(int a, int b)
{
	if (a > b)
		return a;
	else
		return b;
}

struct Node* newNode(int kluch)
{
	struct Node *node = (struct Node *)
	malloc(sizeof(struct Node));
	node->kluch = kluch;
	node->levoe = NULL;
	node->pravoe = NULL;
	node->visota = 1;
	return (node);
}

struct Node* rgtRotate(struct Node *y)
{
	struct Node *x = y->levoe;
	struct Node *T2 = x->pravoe;
	x->pravoe = y;
	y->levoe = T2;
	y->visota = max(height(y->levoe), height(y->pravoe)) + 1;
	x->visota = max(height(x->levoe), height(x->pravoe)) + 1;
	return x;
}

struct Node* lftRotate(struct Node *x)
{
	struct Node *y = x->pravoe;
	struct Node *T2 = y->levoe;
	y->levoe = x;
	x->pravoe = T2;
	x->visota = max(height(x->levoe), height(x->pravoe)) + 1;
	y->visota = max(height(y->levoe), height(y->pravoe)) + 1;
	return y;
}

int getBalance(struct Node *N)
{
	if (N == NULL)
		return 0;
	return height(N->levoe) - height(N->pravoe);
}

struct Node* dobavlenie(struct Node *node, int kluch)
{
	if (node == NULL)
		return (newNode(kluch));
	if (kluch < node->kluch)
		node->levoe = dobavlenie(node->levoe, kluch);
	else if (kluch > node->kluch)
		node->pravoe = dobavlenie(node->pravoe, kluch);
	else
		return node;
	node->visota = 1 + max(height(node->levoe),
		height(node->pravoe));
	int balance = getBalance(node);
	if (balance > 1 && kluch < node->levoe->kluch)
		return rgtRotate(node);
	if (balance < -1 && kluch > node->pravoe->kluch)
		return lftRotate(node);
	if (balance > 1 && kluch > node->levoe->kluch)
	{
		node->levoe = lftRotate(node->levoe);
		return rgtRotate(node);
	}

	if (balance < -1 && kluch < node->pravoe->kluch)
	{
		node->pravoe = rgtRotate(node->pravoe);
		return lftRotate(node);
	}
	return node;
}

struct Node* minValueNode(struct Node *node)
{
	struct Node *current = node;
	while (current->levoe != NULL)
		current = current->levoe;
	return current;
}

void inOrderWithHeights(struct Node *base)
{
	if (base != NULL)
	{
		inOrderWithHeights(base->levoe);
		printf("%d, Naxoditsa na visote %d\n", base->kluch, base->visota);
		inOrderWithHeights(base->pravoe);
	}
}

void inOrder(struct Node *base)
{
	if (base != NULL)
	{
		inOrder(base->levoe);
		printf("%d ", base->kluch);
		inOrder(base->pravoe);
	}
}

int main()
{
	struct Node *base = NULL;
	base = dobavlenie(base, 40);
	base = dobavlenie(base, 21);
	base = dobavlenie(base, 43);
	base = dobavlenie(base, 12);
	base = dobavlenie(base, 78);
	base = dobavlenie(base, 1);
	base = dobavlenie(base, 4);
	base = dobavlenie(base, 8);
	base = dobavlenie(base, 10);
	inOrder(base);
	printf("\n----------------\n");
	inOrderWithHeights(base);
	return 0;
}
