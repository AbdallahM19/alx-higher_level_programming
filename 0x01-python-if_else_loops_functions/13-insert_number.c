#include "lists.h"
#include <stdlib.h>

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
    listint_t *prev = NULL;

    if (!new_node)
        return (NULL);
    new_node->n = number;
    new_node->next = NULL;
    if (!*head)
    {
        *head = new_node;
        return (new_node);
    }
    while (current && current->n < number)
    {
        prev = current;
        current = current->next;
    }
    if (!prev)
    {
        new_node->next = *head;
        *head = new_node;
    }
    else
    {
        prev->next = new_node;
        new_node->next = current;
    }
    return (new_node);
}
