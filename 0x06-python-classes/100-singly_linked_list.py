#!/usr/bin/python3
"""Define classes for a singly-linked list"""


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.
        Args:
            data (int): The data of the new Node
            next_node (Node): The next node of the new Node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get/set data of the node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """get/set next node of the new node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not 0:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
"""Defines a singly linked list"""

    def __init__(self):
        """Initialize a new Node to the SLL."""
        self.__head = None


