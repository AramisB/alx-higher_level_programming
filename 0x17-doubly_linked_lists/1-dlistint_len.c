#include "lists.h"
/**
 * dlistint_len - return the number of elements in dlistint
 *
 * @h: pointer to the first element
 *
 * Return: number of elements in dlistint
 */
size_t dlistint_len(const dlistint_t *h)
{
	const dlistint_t *tmp = h;
	size_t n = 0;

	while (tmp != NULL)
	{
		n++;
		tmp = tmp->next;
	}
	return (n);
}
