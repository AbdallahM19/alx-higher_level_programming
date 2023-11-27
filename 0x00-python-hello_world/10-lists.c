#include "lists.h"

/**
 * print_list - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_list(const listint_t *h)
{
	const listint_t *current;
	unsigned int n = 0;

	current = h;
	while (current)
	{
		printf("%i\n", current->n);
		current = current->next;
		n++;
	}
	return (n);
}

/**
 * add_node - adds a new node at the beginning of a listint_t list
 * @head: pointer to a pointer of the start of the list
 * @n: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_node(listint_t **head, const int n)
{
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = n;
	new_node->next = *head;
	*head = new_node;

	return (new_node);
}

/**
 * free_list - free a listint_t list
 * @head: pointer to list to be free
 * Return: void
 */
void free_list(listint_t *head)
{
	listint_t *current;

	while (head)
	{
		current = head;
		head = head->next;
		free(current);
	}
}
