class Order:
    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty

    def print(self):
        print("     Customer:", self.getCustomer())
        print("     Quantity:", self.getQtty())

    def getQtty(self):
        return self.qtty

    def getCustomer(self):
        return self.customer


class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

    def getInfo(self):
        return self.info

    def getNext(self):
        return self.next

    def setNext(self, next_node):
        self.next = next_node

class QueueInterface:
    def size(self):
        raise NotImplementedError

    def isEmpty(self):
        raise NotImplementedError

    def front(self):
        raise NotImplementedError

    def enqueue(self, info):
        raise NotImplementedError

    def dequeue(self):
        raise NotImplementedError

class Queue(QueueInterface):
    def __init__(self):
        self.top = None
        self.rear = None
        self.count = 0

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def front(self):
        if self.isEmpty():
            return None
        return self.top.getInfo()

    def enqueue(self, info):
        new_node = Node(info)
        if self.isEmpty():
            self.top = new_node
            self.rear = new_node
        else:
            self.rear.setNext(new_node)
            self.rear = new_node
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            return None
        info = self.top.getInfo()
        self.top = self.top.getNext()
        self.count -= 1
        if self.count == 0:
            self.rear = None
        return info

    def printInfo(self):
        print("********* QUEUE DUMP *********")
        print("   Size:", self.size())

        node = self.top
        i = 1
        while node is not None:
            print(f"   ** Element {i}")
            node.getInfo().print()
            node = node.getNext()
            i += 1


def main():
    q = Queue()

    o1 = Order(20, "cust1")
    o2 = Order(30, "cust2")
    o3 = Order(40, "cust3")
    o4 = Order(50, "cust4")

    q.enqueue(o1)
    q.enqueue(o2)
    q.enqueue(o3)
    q.enqueue(o4)

    q.printInfo()


if __name__ == "__main__":
    main()
