class Node:
    # Node of a singly linked list.
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    # Queue (=FIFO) implementation using linked list.
    def __init__(self):
        self.head = None  # beginning of the queue
        self.tail = None   # end of the queue
        

    def is_empty(self):
        return self.head is None
    

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is not None:
            self.tail.next = new_node
            self.tail = new_node

        if self.head is None:
            self.head = new_node

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")

        value = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return value
