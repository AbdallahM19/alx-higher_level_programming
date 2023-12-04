#include "lists.h"

/**
 * rev_list - reverses linked list
 * @head: pointer head of the linked list
 * Return: new head of the reversed list
 */
void rev_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}

/**
 * compare_lists - compares two linked lists for equality
 * @list1: pointer first linked list
 * @list2: pointer second linked list
 * Return: 1 if lists are equal, 0 if (not equal)
 */
listint_t *compare_lists(listint_t *head)
{
	listint_t *slow = head;
	listint_t *fast = head;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	return (slow);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the linked list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *second_half;

	if (*head == NULL || (*head)->next == NULL)
		return(1);

	slow = compare_lists(*head);
	fast = slow->next;
	rev_list(&fast);
	second_half = *head;

	while (fast && second_half)
	{
		if (fast->n == second_half->n)
		{
			fast = fast->next;
			second_half = second_half->next;
		}
		else
			return(0);
	}
	if (!fast)
		return (1);
	return (0);
}
