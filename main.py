#class for holding the data, defaults to empty node if no data is given
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None #pointer to the next node

# Class for managing the list and nodes
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)

        if self.head == None:  # if the node is empty, the new node is the head
            self.head = node
        else:  # if not empty iterate through items and append new node at the end (tail)
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self.size += 1 #always update the size to prevent costly iterations to get the size

    #defining iteration function to make iterating over nodes in the list possible
    def __iter__(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def get_size(self):
        return self.size

    '''Exercise Part 1,2 and 3:
    Implement the given methods below according to the requirements in the exercise sheet.
    return the correct data types and values'''

    def clear(self):
        while (self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None
        return

    def get_data(self, data):
        current = self.head
        while current != None:
            if current.data == data:
                print(data)
                return data
            current = current.next
        else:
            return False

    def delete(self, data):
        prev = None
        current = self.head

        while current != None:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                self.size -= 1
                return
            prev = current
            current = current.next

    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data),
            temp = temp.next

list1 = SinglyLinkedList()
list1.append(4)
list1.append(5)
list1.append(7)
list1.append(9)



'''Exercise Part 4: Copy the code from the singly linked list implementation and rewrite it
    to implement a doubly linked list according to the exercise sheet. Dont forget to change the names of the classes
    in the code to reflect the new class name (NodeDLL instead of Node).'''


class NodeDLL:
    def __init__(self, data=None):
        self.data = data
        self.next = None    # pointer to the next node
        self.prev = None    # pointer to the previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = NodeDLL(data)
        node.prev = self.tail

        if self.tail == None:  # if the node is empty, the new node is the head
            self.head = node
            self.tail = node
            node.next = None
        else:  # if not empty iterate through items and append new node at the end (tail)
            self.tail.next = node
            node.next = None
            self.tail = node
        self.size += 1 #always update the size to prevent costly iterations to get the size

    def __iter__(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def clear(self):
        while (self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None
        return

    def get_data(self, data):
        current = self.head
        while current != None:
            if current.data == data:
                print(data)
                return data
            current = current.next
        else:
            return False

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data and current == self.head:
               if not current.next:
                    current = None
                    self.head = None
                    self.size -= 1
                    return
               else:
                    next = current.next
                    current.next = None
                    next.prev = None
                    current = None
                    self.head = next
                    self.size -= 1
                    return
            elif current.data == data:
                if current.next:
                    next = current.next
                    prev = current.prev
                    prev.next = next
                    next.prev = prev
                    current.next = None
                    current.prev = None
                    current = None
                    self.size -= 1
                    return
                else:
                    prev = current.prev
                    prev.next = None
                    current.prev = None
                    current = None
                    self.size -= 1
                    return
            current = current.next

    def get_size(self):
        return self.size

    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data),
            temp = temp.next

list2 = DoublyLinkedList()
list2.append(1)
list2.append(2)
list2.append(4)




'''Exercise Part 5 and 6:
    #Complete the classes below to implement a stack and queue data structure. You are free to use built-in
    #methods but you have to complete all methods below. Always return the correct data type according
    #to the exercise sheet'''

class MyStack:

    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)
        return self.items

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

list3 = MyStack()
list3.push(4)
list3.push(2)
list3.push("hello")


class MyQueue:

    def __init__(self):
        self.items = []

    def push(self,element):
        self.items.insert(0,element)
        return

    def pop(self):
        return self.items.pop()

    def show_left(self):
        return self.items[0]

    def show_right(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

list4 = MyQueue()
list4.push("hi")
list4.push(5)
list4.push(4)

