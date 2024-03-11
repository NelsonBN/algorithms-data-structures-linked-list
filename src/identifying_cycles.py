class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def identifying_cycles(head: Node) -> bool:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


head1 = Node(10)

node1_1 = Node(20)
head1.next = node1_1

node1_2 = Node(30)
node1_1.next = node1_2

node1_3 = Node(40)
node1_2.next = node1_3

node1_4 = Node(50)
node1_3.next = node1_4

node1_5 = Node(60)
node1_4.next = node1_5

node1_6 = Node(70)
node1_5.next = node1_6

node1_7 = Node(80)
node1_6.next = node1_7

node1_5.next = node1_3




head2 = Node(10)

node2_1 = Node(20)
head2.next = node2_1

node2_2 = Node(30)
node2_1.next = node2_2

node2_3 = Node(40)
node2_2.next = node2_3

node2_4 = Node(50)
node2_3.next = node2_4

node2_5 = Node(60)
node2_4.next = node2_5

node2_6 = Node(70)
node2_5.next = node2_6

node2_7 = Node(80)
node2_6.next = node2_7



print(identifying_cycles(head1))
print(identifying_cycles(head2))
