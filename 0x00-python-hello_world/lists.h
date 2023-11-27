#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_s - singly link list
 * @n: int
 * @next: points to next node
 * Description: singly linked list node structure
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

int check_cycle(listint_t *list);
size_t print_list(const listint_t *h);
listint_t *add_node(listint_t **head, const int n);
void free_list(listint_t *head);

#endif /* LISTS_H */
