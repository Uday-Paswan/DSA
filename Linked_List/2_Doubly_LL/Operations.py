class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None 
        self.next = None

def traverse_forward(head):
    current = head
    while current is not None:
        print(current.data, end=" ")
        current = current.next

def traverse_backward(head):
    if head is None:
        return 
    current = head
    while current.next is not None: 
        current = current.next
    while current is not None: 
        print(current.data, end=" ") 
        current = current.prev

def insert_begin(head, data): 
    new_node = Node(data) 
    new_node.next = head 
    if head is not None: 
        head.prev = new_node 
    head = new_node
    return head

def insert_end(head, data):
    new_node = Node(data) 
    if head is None: 
        return new_node 
    current = head 
    while current.next is not None: 
        current = current.next 
    current.next = new_node 
    new_node.prev = current 
    return head

def insert_position(head, position, data):
    if position == 1:
        return insert_begin(head, data)

    current = head

    for _ in range(position - 2):
        if current is None:
            return head
        current = current.next

    if current is None:
        return head

    if current.next is None:
        return insert_end(head, data)

    new_node = Node(data)

    new_node.next = current.next
    current.next.prev = new_node
    new_node.prev = current
    current.next = new_node

    return head

def delete_head(head):
    if head is None:
        return None

    head = head.next

    if head is not None:
        head.prev = None

    return head


def delete_tail(head):
    if head is None:
        return None

    if head.next is None:
        return None

    current = head

    while current.next is not None:
        current = current.next

    current.prev.next = None

    return head


def delete_position(head, position):
    if head is None:
        return None

    if position == 1:
        return delete_head(head)

    current = head

    for _ in range(position - 1):
        if current is None:
            return head
        current = current.next

    if current is None:
        return head

    if current.next is None:
        return delete_tail(head)

    current.prev.next = current.next
    current.next.prev = current.prev

    return head