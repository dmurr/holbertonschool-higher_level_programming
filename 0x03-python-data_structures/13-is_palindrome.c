#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * value_at_index - find node at nth index
 * @head: head of list
 * @index: node position
 *
 * Return: pointer to node at index
 */
int value_at_index(listint_t *head, unsigned int index)
{
	listint_t *temp;
	unsigned int i = 0;

	if (!head)
		return (0);

	temp = head;
	while (i < index)
	{
		if (!temp->next)
			return (0);
		temp = temp->next;
		i++;
	}

	return (temp->n);
}

/**
 * is_palindrome - Finds whether linkes list is a palindrome
 * @head: pointer to list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	unsigned int first = 0, last = 0;

	if (*head == NULL)
		return (1);

	temp = *head;
	while (temp->next)
	{
		last += 1;
		temp = temp->next;
	}
	for (; first < last; first++, last--)
	{
		if (value_at_index(*head, first) != value_at_index(*head, last))
		{
			return (0);
		}
	}
	return (1);

}
