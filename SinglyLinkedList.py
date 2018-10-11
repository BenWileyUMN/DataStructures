# Implementation and Display of Singly Linked List in Python
# Ben Wiley

class Node:
        def __init__(self, value, next):
            self.value = value
            self.next = next


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def addAfter(self, addAfterVal, newNode):
        if self.head == None:
            self.head = newNode
        else:
            checkNode = self.head
            while checkNode != None and checkNode.value != addAfterVal:
                checkNode = checkNode.next
            if checkNode == None:
                raise ValueError("Could not find value to add node after...")
            else:
                tmpNext = checkNode.next
                checkNode.next = newNode
                checkNode.next.next = tmpNext

    def valueIsInLinkedList(self, value):
        checkNode = self.head
        while checkNode.value != value and checkNode != None:
            checkNode = checkNode.next
        if checkNode.value == value:
            return True
        return False

    def deleteNode(self, value):
        checkNode = self.head
        while checkNode.next.value != value and checkNode != None:
            checkNode = checkNode.next
        if checkNode.next.value == value:
            checkNode.next = checkNode.next.next
        else:
            raise ValueError("Could not find node to delete...")

    # Print a Representation of Linked List for Test Class Below
    def printRepresentationOfLinkedList(self):
        checkNode = self.head
        print("head --> ", end='')
        while checkNode != None:
            print("| {} | -|--> ".format(checkNode.value), end='')
            checkNode = checkNode.next
        print(" None")

    
class TestSinglyLinkedList:
    
    def __init__(self):
        self.linkedList = SinglyLinkedList()

    def createTwoNodes(self):
        node1 = Node("1", None)
        self.linkedList.addAfter(None, node1)
        node2 = Node("2", None)
        self.linkedList.addAfter(node1.value, node2)

        self.linkedList.printRepresentationOfLinkedList()

    def addOneBetweenOneAndTwo(self):
        node3 = Node("3", None)
        self.linkedList.addAfter("1", node3)

        print("\nAfter adding node w/ 3 after node 1: ")
        self.linkedList.printRepresentationOfLinkedList()

    def deleteNode3(self):
        self.linkedList.deleteNode("3")

        print("\nShould have deleted node w/ value of 3: ")
        self.linkedList.printRepresentationOfLinkedList()

def main():
    test = TestSinglyLinkedList()
    test.createTwoNodes()
    test.addOneBetweenOneAndTwo()
    test.deleteNode3()

if __name__ == '__main__':
    main()

