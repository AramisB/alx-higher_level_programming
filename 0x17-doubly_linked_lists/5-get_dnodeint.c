#include "lists.h"
/**
 * get_dnodeint_ata_index - returns the nth node of a dlistint
 *
 * @head: pointer to the first node
 * @index: index of the node
 *
 * Return: the index of the node or NULL if the node does not exist
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	dlistint_t *current = head;
	unsigned int count = 0;

	while (current != NULL)
	{
		if (count == index)
		{
			return (current);
		}
		count++;
		current = current->next;
	}
	return (NULL);
}
