class Node:
    """Class representing a node in the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Class representing the linked list."""
    def __init__(self):
        self.head = None

#     def add_at_beginning(self, data):
#         """Add a node at the beginning of the linked list."""
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
#         return f"Added {data} at the beginning."

#     def add_at_end(self, data):
#         """Add a node at the end of the linked list."""
#         new_node = Node(data)
# #  It will fail because self.head is None, and you cannot access current.next on a None object.
# # This would result in an AttributeError.


#         if not self.head:
#             self.head = new_node
#             return f"Added {data} as the first node."
#         current = self.head
#         while current.next:
#             current = current.next
#         current.next = new_node
#         return f"Added {data} at the end."
    def add_at_beginning(self, data):
        """Add a node at the beginning of the linked list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return f"Added {data} at the beginning."

    def add_at_end(self, data):
        """Add a node at the end of the linked list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return f"Added {data} as the first node."
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        return f"Added {data} at the end."

    def update_node(self, old_data, new_data):
        """Update a node's value in the linked list."""
        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                return f"Updated node from {old_data} to {new_data}."
            current = current.next
        return f"Node with data {old_data} not found."

    def delete_node(self, data):
        """Delete a node from the linked list."""
        current = self.head
        if current and current.data == data:
            self.head = current.next
            return f"Deleted node with data {data}."
        prev = None
        while current:
            if current.data == data:
                prev.next = current.next
                return f"Deleted node with data {data}."
            prev = current
            current = current.next
        return f"Node with data {data} not found."

    def get_data(self):
        """Retrieve all data from the linked list."""
        data_list = []
        current = self.head
        while current:
            data_list.append(current.data)
            current = current.next
        return data_list
    
    def reverse_linked_list(self):
        """Reverse the linked list into a new list."""
        current = self.head
        data_list = []
        while current:
            data_list.append(current.data)
            current = current.next
        reversed_list = LinkedList()
        for data in data_list[::-1]:  # Reverse the data list using slicing
            reversed_list.add_at_end(data)
        return reversed_list
    
    def sorted_linked_list(self):
        """Sort the linked list and return a new sorted linked list."""
        current = self.head
        data_list = []

        # Collect all the data from the linked list
        while current:
            data_list.append(current.data)
            current = current.next
        
        # Sort the data list
        sorted_data = sorted(data_list)

        # Create a new linked list with sorted data
        sorted_list = LinkedList()
        for data in sorted_data:
            sorted_list.add_at_end(data)

        return sorted_list
#add a data node