class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_beginning(self, value: int):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def add_at_end(self, value: int):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def update_node(self, target_value: int, new_value: int) -> bool:
        current = self.head
        while current:
            if current.value == target_value:
                current.value = new_value
                return True
            current = current.next
        return False

    def delete_node(self, value: int) -> bool:
        current = self.head
        prev = None
        while current:
            if current.value == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def to_list(self) -> list:
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result
