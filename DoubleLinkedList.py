class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    # Add to the list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = self.current = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # Remove by id
    def remove_by_id(self, id):
        current_node = self.head
        while current_node:
            if current_node.data['id'] == id:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                if current_node == self.head:
                    self.head = current_node.next
                if current_node == self.tail:
                    self.tail = current_node.prev
                return True
            current_node = current_node.next
        return False

    # Find an element by route or id
    def find(self, search_term):
        current_node = self.head
        while current_node:
            if (search_term in current_node.data['route']) or (current_node.data['id'] == search_term):
                return current_node.data
            current_node = current_node.next
        return None

    # Remove the last node
    def remove_last(self):
        if not self.tail:
            return False
        last_trip = self.tail
        if last_trip.prev:
            last_trip.prev.next = None
        self.tail = last_trip.prev
        return last_trip.data

    # Convert the linked list to a list
    def to_array(self):
        result = []
        current_node = self.head
        while current_node:
            result.append(current_node.data)
            current_node = current_node.next
        return result

    # Update a trip's status based on its id
    def update_trip_status(self, id, status):
        current_node = self.head
        while current_node:
            if current_node.data['id'] == id:
                current_node.data['status'] = status
                return True
            current_node = current_node.next
        return False

    # Clear all nodes
    def clear_all(self):
        self.head = None
        self.tail = None
        self.current = None

    # Peek at the first element
    def peek(self):
        return self.head.data if self.head else None
