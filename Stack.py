# Implementation of a Stack In Python
# Ben Wiley

class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top == None

    def push(self, value):
        if self.isEmpty():
            self.top = Node(value, None)
        else:
            self.top = Node(value, self.top)

    def pop(self):
        if self.isEmpty():
            raise ValueError("Can't pop an empty stack...")
        else:
            self.top = self.top.next
    
    def peek(self):
        if self.isEmpty():
            raise ValueError("Can't peak an empty stack...")
        else:
            return self.top.value

    def printRepresentationOfStack(self):
        checkNode = self.top
        print("Top")
        while checkNode != None:
            print("_____")
            print("| {} |".format(checkNode.value))
            print("_____")
            checkNode = checkNode.next
        print("\nBottom")


class StackTester:

    def __init__(self):
        self.stack = Stack()

    def pushTwoNodesOntoStack(self):
        self.stack.push("1")
        self.stack.push("2")

        print("Pushed Two Nodes Onto Stack: ")
        self.stack.printRepresentationOfStack()

    def popOneNode(self):
        self.stack.pop()

        print("\nPopped One Node Off Stack:")
        self.stack.printRepresentationOfStack()

    def pushNodeThreeOnStack(self):
        self.stack.push("3")

        print("\nPushed 3 Onto the Top Of Stack:")
        self.stack.printRepresentationOfStack()


def main():
    test = StackTester()
    test.pushTwoNodesOntoStack()
    test.popOneNode()
    test.pushNodeThreeOnStack()

if __name__ == '__main__':
    main()
