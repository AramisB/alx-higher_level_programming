#include "lists.h"
/**
 * free_dlistint - frees the dlistint list
 *
 * @head: pointer to the first element
 */
void free_dlistint(dlistint_t *head)
{
	dlistint_t *free_node;
	
	while(head != NULL)
	{
		free_node = head;
		head = head->next;
		free(free_node);
	}
}

