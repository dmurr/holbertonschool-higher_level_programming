#include "lists.h"

/**
 * insert_node - adds a new node into a sorted list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *current;

	if (!head)
		return (NULL);

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);

	newnode->n = number;
	newnode->next = NULL;

	current = *head;

	if (number < current->n)
	{
		newnode->next = current;
		*head = newnode;
		return (newnode);
	}

	while (number > current->next->n)
	{
		current = current->next;
		if (current->next == NULL)
		{
			current->next = newnode;
			return (newnode);
		}
	}

	newnode->next = current->next;
	current->next = newnode;

	return (newnode);
}
