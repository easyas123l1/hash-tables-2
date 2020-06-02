class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    def find(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None

    def delete(self, value):
        current = self.head
        if current.value == value:
            self.head = current.next
            return current
        while current.next is not None:
            if current.next == value:
                temp = current.next
                current.next = current.next.next
                return temp
            current = current.next
        return None


if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_head(Node(11))
