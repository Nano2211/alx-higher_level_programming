#ifndef LIST_H
#define LIST_H

#include <stdlib.h>

typedef struct listint_s
/**
 * listint_s - singly linked list
 * @a: integer
 * @n: points to node
 *
 * Description: a singly linked list node structure
 */
{
	int a;
	struct listint_s *n;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
