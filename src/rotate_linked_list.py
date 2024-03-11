class Node:
    def __init__(self, data, node = None):
        self.data = data
        if node:
            self.next = node
        else:
            self.next = node

def print_linked_list(head: Node):
    print("**** Printing linked list ****")
    pointer = head
    while pointer:
        print(pointer.data)
        pointer = pointer.next
    print("**** End ****")


def rotate_linked_list(node: Node) -> Node:
    aux = None
    while node:
        next = node.next
        node.next = aux
        aux = node
        node = next
    return aux


head = Node(10,
    Node(20,
        Node(30,
            Node(40,
                Node(50,
                    Node(60))))))

print_linked_list(head)
head = rotate_linked_list(head)
print_linked_list(head)
