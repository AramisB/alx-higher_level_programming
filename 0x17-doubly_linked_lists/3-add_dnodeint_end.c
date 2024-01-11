#include "lists.h"
/**
 * add_dnodeint_en - adds a node to the end of a list
 *
 * @head: pointer to the pointer of the first node
 * @n: data of the new node
 *
 * Return: address of the new element or NULL if it failed
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *last_node;
	dlistint_t *temp = *head;

	last_node = malloc(sizeof(dlistint_t));

	if (last_node == NULL)
	{
		return (NULL);
	}
	last_node->n = n;
	last_node->next = NULL;

	if (*head == NULL)
	{
		last_node->prev = NULL;
		*head = last_node;
	}
	else
	{
		while(temp->next != NULL)
		{
			temp = temp->next;
		}
		temp->next = last_node;
		last_node->prev = temp;
	}
	return (last_node);
}
