#include "lists.h"

/**
 * check_cycle - check the list have a cycle or no
 * @list: pointer to the list
 * Return: 0 or 1
*/

int check_cycle(listint_t *list)
{
	listint_t *S = list, *F = list;

	while (S && F && F->next)
	{
		S = S->next;
		F = F->next->next;
		if (S == F)
			return (1);
	}
	return (0);
}
