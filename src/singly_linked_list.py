class Node:
    def __init__(self, data, node = None):
        self.data = data
        if node:
            self.next = node
        else:
            self.next = node


head = Node(0,
        Node(10,
            Node(20,
                Node(30,
                    Node(40)
                )
            )
        )
    )


dummy = head
while dummy:
    print(dummy.data)
    dummy = dummy.next
