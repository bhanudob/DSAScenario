"""
shipment_linked_list.py

This file contains the Node class and ShipmentLinkedList class definitions.
Students will complete the methods for:
1. Insert at start
2. Insert at end
3. Insert at a specific position
4. Delete by ID
5. Search by ID

Each method has a 'TODO' comment where you will add your code.
"""
from tables.nodes.filenode import new_node


class Node:
    """
    Represents a single shipment node in the linked list.
    Attributes:
        shipment_id (int): Unique ID of the shipment.
        next (Node): Pointer to the next Node in the list.
    """
    def __init__(self, shipment_id):
        self.shipment_id = shipment_id
        self.next = None


class ShipmentLinkedList:
    """
    A singly linked list for managing shipments.

    Methods to implement:
        - insert_at_start(self, shipment_id)
        - insert_at_end(self, shipment_id)
        - insert_at_position(self, shipment_id, position)
        - delete_by_id(self, shipment_id)
        - search_by_id(self, shipment_id)
    """

    def __init__(self):
        self.head = None

    def insert_at_start(self, shipment_id):
        """
        Insert a new Node with 'shipment_id' at the start of the list.
        TODO: Implement pointer manipulation for head insertion.
        """
        # TODO: Write your code here
        new_node = Node(shipment_id)
        new_node.next = self.head
        self.head = new_node
        # Steps (hint):
        # 1. Create a new Node.
        # 2. Point new_node.next to current head.
        # 3. Update head to new_node.
        pass

    def insert_at_end(self, shipment_id):
        """
        Insert a new Node with 'shipment_id' at the end of the list.
        TODO: Implement pointer traversal to reach the end and insert.
        """
        # TODO: Write your code here
        new_node = Node(shipment_id)
        # Steps (hint):
        # 1. Create a new Node.
        # 2. If the list is empty, make new_node the head.
        # 3. Otherwise, traverse until you reach the last node.
        # 4. Set last_node.next to new_node.
        pass

    def insert_at_position(self, shipment_id, position):
        """
        Insert a new Node with 'shipment_id' at the specified 0-based position.
        If position is 0 or less, treat it as insert_at_start.
        If position is beyond the current length, insert at end.
        TODO: Implement pointer manipulation to insert at 'position'.
        """
        # TODO: Write your code here
        # Steps (hint):
        # 1. If position <= 0: call insert_at_start(...)
        # 2. Traverse until you find the (position-1)-th node or the end.
        # 3. Insert the new node by adjusting pointers.
        pass

    def delete_by_id(self, shipment_id):
        """
        Delete the first occurrence of 'shipment_id' in the list.
        TODO: Implement pointer manipulation to remove the node.
        Return True if deletion succeeded, False if not found.
        """
        # TODO: Write your code here
        # Steps (hint):
        # 1. Check if the list is empty.
        # 2. If the head node matches, update head.
        # 3. Otherwise, traverse until you find the node to delete (track prev).
        # 4. Adjust prev.next to skip the found node.
        # 5. Return True if deleted, False if not found.
        pass

    def search_by_id(self, shipment_id):
        """
        Search for 'shipment_id' in the list.
        Return the Node if found, otherwise None.
        """
        # TODO: Write your code here
        # Steps (hint):
        # 1. Traverse the list from the head.
        # 2. Compare node.shipment_id with the target.
        # 3. Return the node if a match is found, else None after the loop.
        pass

    def print_list(self):
        """
        Utility function to print all shipment IDs in the list for debugging.
        (No need to modify this unless you want to enhance output.)
        """
        current = self.head
        elements = []
        while current:
            elements.append(str(current.shipment_id))
            current = current.next
        print(" -> ".join(elements))
