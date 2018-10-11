# Implementation of a Linear, Singly Linked List Queue 
# Ben Wiley

class Node:
        def __init__(self, value, next):
            self.value = value
            self.next = next


class SinglyLinkedListQueue:

    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front == None and self.rear == None

    def enqueue(self, value):
        if self.isEmpty():
            self.front = Node(value, None)
            self.rear = self.front
        else:
            self.rear.next = Node(value, self.front.next)

    def dequeue(self):
        if self.isEmpty():
            raise ValueError("Can't dequeue an empty queue...")
        else:
            self.front = self.front.next

    def valueIsInQueue(self, value):
        checkNode = self.front
        while checkNode.value != value and checkNode != None:
            checkNode = checkNode.next
        if checkNode == None:
            return False
        return True

    # Print a Representation of Linked List for Test Class Below
    def printRepresentationOfLinkedList(self):
        checkNode = self.front
        print("front --> ", end='')
        while checkNode != None:
            print("| {} | -|--> ".format(checkNode.value), end='')
            checkNode = checkNode.next
        print(" Rear")

    
class TestSinglyLinkedList:
    
    def __init__(self):
        self.queue = SinglyLinkedListQueue()

    def enqueueTwice(self):
        self.queue.enqueue("1")
        self.queue.enqueue("2")

        self.queue.printRepresentationOfLinkedList()

    def dequeue1(self):
        self.queue.dequeue()

        print("\nShould have dequeued node w/ value of 1: ")
        self.queue.printRepresentationOfLinkedList()

    def shouldNotFind3(self):
        boolShouldBeFalse = self.queue.valueIsInQueue("3")
        print("Bool for finding 3 is: ", boolShouldBeFalse)

def main():
    test = TestSinglyLinkedList()
    test.enqueueTwice()
    test.dequeue1()
    test.shouldNotFind3()

if __name__ == '__main__':
    main()