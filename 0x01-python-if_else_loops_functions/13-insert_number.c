#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: double pointer to head node of the linked list
 * @number: number to insert
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *current = *head;

	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (!current || new_node->n < current->n)
	{
		new_node->next = current;
		return(*head = new_node);
	}
	while (current)
	{
		if (!current->next || new_node->n < current->next->n)
		{
			new_node->next = current->next;
			current->next = new_node;
			return (current);
		}
		current = current->next;
	}
	return (NULL);
}
