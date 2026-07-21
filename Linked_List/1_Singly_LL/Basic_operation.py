class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def create_linked_list(arr):
    if not arr:
        return None

    head = Node(arr[0])
    current = head

    for i in range(1, len(arr)):
        new_node = Node(arr[i])
        current.next = new_node
        current = current.next

    return head


def print_linked_list(head):
    current = head

    while current is not None:
        print(current.data)
        current = current.next

def insert_at_beginning(head, data):

    new_node = Node(data)

    new_node.next = head

    head = new_node

    return head

def insert_at_end(head, data):

    new_node = Node(data)

    if head is None:
        return new_node

    current = head

    while current.next is not None:
        current = current.next

    current.next = new_node

    return head

def insert_at_position(head, data, pos):

    if pos == 1:
        return insert_at_beginning(head, data)

    new_node = Node(data)

    current = head

    for i in range(pos - 2):
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return head


arr = [10, 20, 30, 40]

head = create_linked_list(arr)

print_linked_list(head)