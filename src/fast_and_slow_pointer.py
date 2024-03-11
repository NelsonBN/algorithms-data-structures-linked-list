class Node:
    def __init__(self, data, node = None):
        self.data = data
        if node:
            self.next = node
        else:
            self.next = node

def show(head: Node):
    print("**** Printing linked list ****")
    pointer = head
    while pointer:
        print(pointer.data)
        pointer = pointer.next
    print("**** End ****")


def middle_node(head: Node) -> Node:
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    if fast:
        return slow.next

    return slow


head1 = Node(10,
    Node(20,
        Node(30,
            Node(40,
                Node(50,
                    Node(60))))))

head2 = Node(11,
    Node(22,
        Node(33,
            Node(44,
                Node(55,
                    Node(66,
                        Node(77,
                            Node(88,
                                Node(99)))))))))

show(middle_node(head1))
show(middle_node(head2))
