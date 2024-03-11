class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def clear(self): # O(1)
        self.head = None


    def append(self, data): # # O(N)
        if self.head:
            pointer = self.head
            while pointer.next: # # O(N)
                pointer = pointer.next

            pointer.next = Node(data)
        else:
            self.head = Node(data)


    def delete(self, index): # # O(N)
        if index == 0:
            self.head = self.head.next

        else:
            pointer = self[index - 1] # # O(N)
            pointer.next = pointer.next.next


    def insert(self, index, data): # # O(N)
        node = Node(data)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self[index - 1] # # O(N)
            node.next = pointer.next
            pointer.next = node


    def __len__(self): # # O(N)
        count = 0
        pointer = self.head
        while pointer:
            count += 1
            pointer = pointer.next
        return count


    def __getitem__(self, index): # # O(N)
        pointer = self.head
        while index > 0: # # O(N)
            pointer = pointer.next
            index -= 1

        return pointer


    def __setitem__(self, index, data): # # O(N)
        pointer = self[index]
        pointer.data = data


def print_linked_list(linked_list: LinkedList):
    print("**** Printing linked list ****")
    pointer = linked_list.head
    while pointer:
        print(pointer.data)
        pointer = pointer.next
    print("**** End ****")



linked_list = LinkedList()
linked_list.append(0)
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.append(50)

print_linked_list(linked_list)

linked_list.delete(4)

print_linked_list(linked_list)

linked_list.insert(4, 41)

print_linked_list(linked_list)

linked_list[2] = 23

print_linked_list(linked_list)

print(len(linked_list))

linked_list.clear()
print_linked_list(linked_list)
