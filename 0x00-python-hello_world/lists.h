#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * listint_s - singly linked list
 * @n: integer
 * @next: node pointer
 *
 * Desc: singly lined list with node structures
 */

typedef struct listint_s
{

int n;

struct listint_s *next;

} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
