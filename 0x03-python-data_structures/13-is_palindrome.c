#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *current = *head;
    int count = 0, i, j, arr[100000];

    if (*head == NULL || (*head)->next == NULL)
        return (1);
    while (current != NULL)
    {
        current = current->next;
        count++;
    }
    current = *head;
    for (i = 0; i < count; i++)
    {
        arr[i] = current->n;
        current = current->next;
    }
    for (i = 0, j = count - 1; i < count / 2; i++, j--)
    {
        if (arr[i] != arr[j])
            return (0);
    }
    return (1);
}
