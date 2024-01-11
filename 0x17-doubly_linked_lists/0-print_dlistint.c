#include "lists.h"
/**
 * print_dlistint - prints the elements of dlistint
 *
 * @h: pointer to the first element in the list
 *
 * Return: number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *tmp = h;
	size_t n = 0;

	while (tmp != NULL)
	{
		printf("%d\n", tmp->n);
		n++;
		tmp = tmp->next;
	}
	return (n);
}
